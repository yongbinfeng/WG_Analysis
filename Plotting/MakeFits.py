import ROOT
import uuid
import os
import time
import subprocess
ROOT.PyConfig.IgnoreCommandLineOptions = True
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument( '--baseDir',  dest='baseDir', required=True, help='path to workspace directory' )
parser.add_argument( '--outputDir',  dest='outputDir', required=False, default=None, help='name of output diretory for cards' )
parser.add_argument( '--doStatTests',  dest='doStatTests', default=False, action='store_true', help='run statistical tests of WGamma background' )
parser.add_argument( '--doWJetsTests',  dest='doWJetsTests', default=False, action='store_true', help='run tests of Wjets background' )
parser.add_argument( '--doFinalFit',  dest='doFinalFit', default=False, action='store_true', help='run fit to data and background' )
parser.add_argument( '--doToyDataFit',  dest='doToyDataFit', default=False, action='store_true', help='run fit to toy data and background' )
parser.add_argument( '--combineDir',  dest='combineDir', default=None, help='path to combine directory' )

options = parser.parse_args()

_LUMI = 36000.

def main() :

    key_wgamma = 'workspace_wgamma'
    key_signal = 'workspace_signal'
    key_wjets  = 'workspace_wjets'
    key_data   = 'workspace_data'


    #bins = ['mu_EB', 'mu_EE', 'el_EB', 'el_EE']
    bins = [
        {'channel' : 'mu', 'eta' : 'EB' },
    ]

    if options.outputDir is not None :
        if not os.path.isdir( options.outputDir ) :
            os.makedirs( options.outputDir )


    #signal_points = [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3500, 4000]
    signal_points = [200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800]
    #signal_points = [200, 250, 300, 350, 400, 450, 500, 600, 700, 800]

    #generate_card( options.baseDir, 'workspace_toy', 'workspace_signal', signal_pred, options.outputCard )
    if options.doToyDataFit :

        kine_vars = [ { 'name' : 'mt_incl_lepph_z', 'color' : ROOT.kBlue},
                     { 'name' : 'm_incl_lepph_z' , 'color' : ROOT.kRed },
                     { 'name' : 'mt_fulltrans'   , 'color' : ROOT.kBlack },
                     { 'name' : 'mt_constrwmass' , 'color' : ROOT.kGreen },
                     { 'name' : 'ph_pt'          , 'color' : ROOT.kMagenta },
                   ]


        workspace_toy = ROOT.RooWorkspace( 'workspace_toy' )

        for var in kine_vars :
            wgamma_entry = get_workspace_entry( 'wgamma', 'mu', 'EB', var['name'] )
            wjets_entry  = get_workspace_entry( 'wjets', 'mu', 'EB', var['name'] )

            #generate_toy_data( options.baseDir, [key_wgamma, key_wjets], [wgamma_entry, wjets_entry], workspace_toy, suffix='mu_EB' )
            generate_toy_data( options.baseDir, [key_wgamma], [wgamma_entry], workspace_toy, suffix='mu_%s_EB' %var['name'] )


        workspace_toy.writeToFile( '%s/%s.root' %( options.baseDir, workspace_toy.GetName() ) )

        #workspace_gauss_signal = ROOT.RooWorkspace('workspace_gauss_signal')
        #make_gauss_signal( options.baseDir, workspace_toysignal )

        all_cards = {}

        for sig_pt in signal_points :
            for var in kine_vars :
                signal_dic = { 'name' : 'Resonance', 
                               'path' : '%s/%s.root' %( options.baseDir, key_signal ), 
                               'wsname' : key_signal, 
                               'hist_base' : 'srhistpdf_MadGraphResonanceMass%d_width0p01' %sig_pt }

                data_dic = { 'path' : '%s/workspace_toy.root' %( options.baseDir), 
                             'wsname' : 'workspace_toy', 
                             'hist_base' : 'toydata' }

                backgrounds = [ 
                               {'name' : 'Wgamma' , 'path' : '%s/%s.root' %( options.baseDir, key_wgamma ), 'wsname' : key_wgamma, 'hist_base' : 'wgamma' }
                              ]
                card_path = options.outputDir + 'wgamma_test_%s_%d.txt' %(var['name'], sig_pt )

                generate_card( options.baseDir, data_dic, signal_dic, backgrounds, bins, var['name'], card_path  )

                all_cards.setdefault(sig_pt, {})
                all_cards[sig_pt][var['name']] =  card_path 

        if options.combineDir is not None :

            jobs = []
            output_files = {}
            for pt, vardic in all_cards.iteritems() :

                output_files.setdefault( pt, {} )

                fname = '%s/run_combine_%d.sh' %(options.outputDir, pt)

                ofile = open( fname, 'w' )
                ofile.write( '#!/bin/tcsh\n' )
                ofile.write( 'cd %s \n' %options.combineDir ) 
                ofile.write( 'eval `scramv1 runtime -csh` \n' ) 

                for var, card in vardic.iteritems() :
                    
                    log_file = '%s/results_%s_%d.txt'%( options.outputDir, var, pt )
                    ofile.write( 'combine -M Asymptotic -m 1000 -t 1 %s >> %s \n'  %( card, log_file ))
                    output_files[pt][var] = log_file

                    ofile.write( ' cd - \n' )
                    ofile.write( 'echo "^.^ FINISHED ^.^" \n' )
                
                    os.system( 'chmod 777 %s/run_combine.sh' %(options.outputDir) )

                ofile.close()

                jobs.append(fname )

            #jdl_name = '%s/job_desc.jdl'  %( options.outputDir )
            #make_jdl( jobs, jdl_name )

            #os.system( 'condor_submit %s' %jdl_name )

            #wait_for_jobs( 'run_combine')

            #os.system( '%s/run_combine.sh' %( options.outputDir ) )

            combine_results = {}
            for var, ptdic in output_files.iteritems() :
                for pt, f in ptdic.iteritems() :
                    result = process_combine_file( f )
                    combine_results.setdefault(pt, {})
                    combine_results[pt][var] = float( result['Observed Limit'].split('<')[1] )

            limit_graphs = []
            leg = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
            for var in kine_vars :

                npoints = len( combine_results[var['name']] )
                limit_graph = ROOT.TGraph( npoints )
                limit_graph.SetName( 'graph_%s' %var['name'] )
                limit_graph.SetLineColor( var['color'] )
                limit_graph.SetLineWidth( 2 )

                for idx, pt in enumerate(signal_points) :
                    limit_graph.SetPoint( idx, pt, combine_results[var['name']][pt])

                leg.AddEntry(limit_graph,  var['name'], 'L' )
                limit_graphs.append( limit_graph )

            can = ROOT.TCanvas( 'limit_result' ,'Limit result' )
            for idx, graph in enumerate(limit_graphs) :
                if idx == 0 :
                    graph.Draw('AL')
                else :
                    graph.Draw('Lsame')


            leg.Draw()

        
            raw_input('cont')






    if options.doStatTests :
        run_statistical_tests( options.baseDir, key_wgamma, 'dijet_wgamma_mu_EB', 100, options.baseDir, suffix='mu_EB' )

    if options.doFinalFit :
        generate_card( options.baseDir, key_data, etc )

    if options.doWJetsTests :

        run_bkg_scale_test( options.baseDir, key_wgamma, 'dijet_wgamma_mu_EB', key_wjets , 'dijet_prediction_wjets_mu_EB' )


    #make_fit_workspace( options.baseDir, key_wgamma )
    #workspace_toysignal = ROOT.RooWorkspace( 'workspace_toysignal' )
    #make_gauss_signal( options.baseDir, workspace_toysignal )
    #workspace_toysignal.writeToFile( '%s/%s.root' %( options.baseDir, workspace_toysignal.GetName() ) )
    #generate_card( options.baseDir, 'workspace_toy', 'workspace_toysignal', signal_pred, options.outputCard )

def get_workspace_entry( process, channel, eta, var ) : 

    if process == 'wjets' :
        return 'dijet_prediction_%s_%s_%s_%s' %( process, channel, var, eta )
    elif process == 'toydata' :
        return '%s_%s_%s_%s' %( process,channel, var, eta )
    elif process.count('ResonanceMass') :
        return '%s_%s_%s_%s' %( process,channel, var, eta )
    else :
        return 'dijet_%s_%s_%s_%s' %( process,channel, var, eta )

def process_combine_file( fname ) :

    ofile = open( fname, 'r' )

    results = {}

    for line in ofile :
        if line.count(':') > 0 :
            spline = line.split(':')
            results[spline[0]] = spline[1].rstrip('\n')

    ofile.close()

    return results


def run_bkg_scale_test( baseDir, const_ws, const_hist, var_ws, var_hist ) :

    ofile_const = ROOT.TFile.Open( '%s/%s.root' %( baseDir, const_ws) )

    ws_const = ofile_const.Get( const_ws )

    ofile_var = ROOT.TFile.Open( '%s/%s.root' %( baseDir, var_ws) )

    ws_var = ofile_var.Get( var_ws )

    xvar = ws_const.var('x')

    norm_const = ws_const.var( '%s_norm' %const_hist)
    pdf_const = ws_const.pdf( const_hist)

    norm_var = ws_var.var( '%s_norm' %var_hist)
    pdf_var = ws_var.pdf( var_hist)

    npoints = 100

    power_res = ROOT.TGraph( npoints )
    power_res.SetName( 'power_res' )
    logcoef_res = ROOT.TGraph( npoints )
    logcoef_res.SetName( 'logcoef_res' )
    chi2_res = ROOT.TGraph( npoints )
    chi2_res.SetName( 'chi2_res' )

    power = ROOT.RooRealVar( 'power_fit', 'power', -9.9, -100, 100)
    logcoef = ROOT.RooRealVar( 'logcoef_fit', 'logcoef', -0.85, -10, 10 )
    func = 'TMath::Power(@0/13000, @1+@2*TMath::Log10(@0/13000))'  
    dijet_fit = ROOT.RooGenericPdf('dijet_fit', 'dijet', func, ROOT.RooArgList(xvar,power, logcoef))

    for i in range( 10, npoints+10 ) :

        var_frac = float(i) 

        tot  = norm_const.getValV() + var_frac*norm_var.getValV()


        vfrac = ROOT.RooRealVar( 'fraciton', 'fraciton', (var_frac*norm_var.getValV()/tot) )


        summed = ROOT.RooAddPdf( 'summed' ,'summed', ROOT.RooArgList( pdf_const, pdf_var ) , ROOT.RooArgList( vfrac ) )

        dataset_summed = summed.generate( ROOT.RooArgSet(xvar), int(tot), ROOT.RooCmdArg( 'Name', 0, 0, 0, 0, 'summed' ) )

        print 'Nevent Wgamma = %f, nevent Wjets = %f, fraction = %f, total = %f, vfrac = %g, ngenerated = %d' %( norm_const.getValV() , norm_var.getValV(), var_frac, tot, vfrac.getValV(), dataset_summed.numEntries() )

        #dijet_fit.fitTo( dataset_summed, ROOT.RooCmdArg('PrintLevel', -1 ) )
        dijet_fit.fitTo( dataset_summed )

        chi2 = dijet_fit.createChi2(dataset_summed.binnedClone(),ROOT.RooFit.Range(xvar.getMin(), xvar.getMax()) )
        chi2_res.SetPoint( i, var_frac, chi2.getVal() )
        power_res.SetPoint( i, var_frac, power.getValV() )
        logcoef_res.SetPoint( i, var_frac, logcoef.getValV() )



    chi2_res.Draw('AL')
    raw_input('cont')
    power_res.Draw('AL')
    raw_input('cont')
    logcoef_res.Draw('AL')
    raw_input('cont')
    
    #frame = xvar.frame()

    #dataset_summed.plotOn( frame )
    #pdf_const.plotOn( frame )
    #pdf_var.plotOn( frame )

    #frame.Draw()
    #raw_input('cont')



def make_gauss_signal( baseDir, workspace ) :


    #x = ROOT.RooRealVar ('x','x',-10,10) ;
    #mean = ROOT.RooRealVar ('mean','Mean of Gaussian',0,-10,10) 
    #sigma = ROOT.RooRealVar ('sigma','Width of Gaussian',3,-10,10) 
    #gauss = ROOT.RooGaussian ('gauss','gauss(x,mean,sigma)',x,mean,sigma) 
    #frame = x.frame() 
    #gauss.plotOn(frame) 
    #frame.Draw() 
    #raw_input('cont')

    xvar = ROOT.RooRealVar( 'x', 'x', 0, 1000 )
    mean = ROOT.RooRealVar( 'mean', 'mean', 300 )
    sigma = ROOT.RooRealVar( 'sigma', 'sigma', 3 )

    #norm = ROOT.RooRealVar( 'signal_norm', 'signal_norm', 1 )

    signal = ROOT.RooGaussian( 'signal', 'signal', xvar, mean, sigma )

    frame = xvar.frame()
    signal.plotOn( frame )
    frame.Draw()
    raw_input('cont')


    getattr( workspace, 'import' ) ( signal )
    #getattr( workspace, 'import' ) ( norm )



def make_fit_workspace( baseDir, workspace_key ) :

    ofile = ROOT.TFile.Open( '%s/%s.root' %( baseDir, workspace_key ) )

    ws = ofile.Get( workspace_key )

    ws.Print()

    pdf_list = ws.allPdfs()
    print pdf_list.getSize()

    for i in range( 0, pdf_list.getSize() ) :
        print pdf_list[i]


def generate_card( baseDir, data_info, signal_info, backgrounds, bins, kine_var, outputCard ) :

    card_entries = []

    section_divider = '-'*100

    card_entries.append( 'imax %d number of bins' %len( bins ) )
    card_entries.append( 'jmax %d number of backgrounds' %len( backgrounds) ) 
    card_entries.append( 'kmax * number of nuisance parameters' )

    card_entries.append( section_divider )

    max_name_len = max( [len(x['name']) for x in backgrounds ] )
    max_path_len = max( [len(x['path']) for x in backgrounds ] )

    all_binids = []
    for ibin in bins :
        bin_id = '%s_%s' %( ibin['channel'], ibin['eta'] )
        all_binids.append(bin_id)

        for bkgdic in backgrounds :
            bkg_entry = get_workspace_entry( bkgdic['hist_base'], ibin['channel'], ibin['eta'], kine_var )
            card_entries.append( 'shapes %s %s %s %s:%s' %( bkgdic['name'].ljust( max_name_len ), bin_id, bkgdic['path'].ljust( max_path_len ), bkgdic['wsname'], bkg_entry ) )

        signal_entry = get_workspace_entry( signal_info['hist_base'], ibin['channel'], ibin['eta'], kine_var )
        data_entry = get_workspace_entry( data_info['hist_base'], ibin['channel'], ibin['eta'], kine_var )
        card_entries.append( 'shapes %s %s %s %s:%s' %( signal_info['name'], bin_id, signal_info['path'], signal_info['wsname'], signal_entry ) )
        card_entries.append( 'shapes data_obs %s %s %s:%s' %( bin_id, data_info['path'], data_info['wsname'], data_entry ) )

    card_entries.append( section_divider )

    card_entries.append( 'bin          ' + '    '.join( all_binids ) )
    card_entries.append( 'observation  ' + '    '.join( ['-1.0']*len(bins) ) )

    card_entries.append( section_divider )

    card_entries.append( 'bin      ' + '    '.join(['    '.join( [x for x in all_binids] )]*( len(backgrounds) + 1 ) ) ) 
    card_entries.append( 'process  ' + '    '.join( ( [signal_info['name']] + [x['name'] for x in backgrounds])*len(bins) ) )
    card_entries.append( 'process  ' + '    '.join( [str(x) for x in range(0, len(backgrounds) +1 ) ]*len(bins) ) )
    card_entries.append( 'rate     ' + '    '.join( ['1.0','1.0' ]*len(bins) ) )

    card_entries.append( section_divider )

    card_entries.append( 'lumi   lnN    ' + '    '.join(['1.05']*len(backgrounds) + ['1.05'] ) )

    card_entries.append( section_divider )

    #for ibin in bins :
    #    card_entries.append( 'logcoef_dijet_Wgamma_%s flatParam' %( ibin ) )
    #    card_entries.append( 'power_dijet_Wgamma_%s flatParam' %( ibin ) )

    if outputCard is not None :
        print 'Write file ', outputCard
        ofile = open( outputCard, 'w' ) 
        for line in card_entries :
            ofile.write( line + '\n' )
        ofile.close()
    else :
        for ent in card_entries :
            print ent


def generate_toy_data( basedir, ws_key_list, hist_key_list, out_ws, suffix='' ) :

    if not isinstance( ws_key_list, list ) :
        ws_key_list = [ws_key_list]
    if not isinstance( hist_key_list, list ) :
        hist_key_list = [hist_key_list]

    pdfs = []
    norms = []
    xvar = None
    for ws_key, hist_key in zip( ws_key_list, hist_key_list ) :

        ofile = ROOT.TFile.Open( '%s/%s.root' %( basedir, ws_key ) )

        ws = ofile.Get( ws_key )

        norms.append(ws.var( '%s_norm' %hist_key ))
        pdfs.append(ws.pdf( hist_key ))

        if xvar is None :
            xvar = ws.var('x')

        ofile.Close()

    if len( pdfs ) == 1 :
        dataset = pdfs[0].generate( ROOT.RooArgSet(xvar), int(norms[0].getValV()), ROOT.RooCmdArg( 'Name', 0, 0, 0, 0, 'toydata_%s' %suffix ) )
    else :
        total = sum( [x.getValV() for x in norms ] )

        fractions = [ x.getValV()/total for x in norms ] 

        pdfList = ROOT.RooArgList()
        for p in pdfs :
            pdfList.add( p )

        fracList = ROOT.RooArgList()
        for f in fractions[:-1] :
            myvar = ROOT.RooRealVar( str(uuid.uuid4()), str(uuid.uuid4()), f )
            myvar.Print()
            fracList.add( myvar )

        summed = ROOT.RooAddPdf( 'summed' ,'summed', pdfList , fracList )
        dataset = summed.generate( ROOT.RooArgSet(xvar), int(total), ROOT.RooCmdArg( 'Name', 0, 0, 0, 0, 'toydata_%s' %suffix ) )

    # not clear why we have to rename here
    getattr( out_ws, 'import' ) ( dataset, ROOT.RooCmdArg('RenameAllNodes', 0, 0, 0, 0, 'toydata_%s' %suffix ) )

def run_statistical_tests( basedir, ws_key, hist_key, niter=100, outputDir=None, suffix='' ) :

    ofile = ROOT.TFile.Open( '%s/%s.root' %( basedir, ws_key ) )

    ws = ofile.Get( ws_key )

    normalization = ws.var( '%s_norm' %hist_key )
    pdf = ws.pdf( hist_key )
    xvar = ws.var('x')
    power = ws.var( 'power_%s' %hist_key )
    logcoef = ws.var( 'logcoef_%s' %hist_key )

    power_val = power.getValV()
    power_err = power.getErrorHi()
    logcoef_val = logcoef.getValV()
    logcoef_err = logcoef.getErrorHi()

    can_stat = ROOT.TCanvas( 'can_stat', '' )

    hist_stat   = ROOT.TH2F( 'hist_stat'  , 'hist_stat'  , 100, power_val - 5*power_err, power_val + 5*power_err, 100, logcoef_val - 5*logcoef_err, logcoef_val + 5*logcoef_err )

    for i in range( 0, niter ) :

        dataset = pdf.generate( ROOT.RooArgSet(xvar), normalization.getValV() )
        dataset.SetName( 'toydata%s%d' %(ws_key, i) )

        pdf.fitTo( dataset, ROOT.RooCmdArg('PrintLevel', -1 ) )

        #frame = xvar.frame()
        #dataset.plotOn(frame)
        #pdf.plotOn(frame)
        #frame.Draw()
        #raw_input('cont')

        hist_stat.Fill( power.getValV(), logcoef.getValV() )

    hist_stat.Draw('colz')
    raw_input('cont')

    prf = hist_stat.ProfileX( 'prf' )
    prf.Draw()
    raw_input('cont')

    if outputDir is not None :
        can_stat.SaveAs( '%s/wgamma_stat_%s.pdf' %( outputDir, suffix) )

def make_jdl( exe_list, output_file ) :

    base_dir = os.path.dirname( output_file )

    file_entries = []
    file_entries.append('#Use only the vanilla universe')
    file_entries.append('universe = vanilla')
    file_entries.append('# This is the executable to run.  If a script,')
    file_entries.append('#   be sure to mark it "#!<path to interp>" on the first line.')
    file_entries.append('# Filename for stdout, otherwise it is lost')
    #file_entries.append('output = stdout.txt')
    #file_entries.append('error = stderr.txt')
    file_entries.append('# Copy the submittor environment variables.  Usually required.')
    file_entries.append('getenv = True')
    file_entries.append('# Copy output files when done.  REQUIRED to run in a protected directory')
    file_entries.append('when_to_transfer_output = ON_EXIT_OR_EVICT')
    file_entries.append('priority=0')
    
    for exe in exe_list :
    
        file_entries.append('Executable = %s' %exe)
        file_entries.append('Initialdir = %s' %base_dir)
        file_entries.append('# This is the argument line to the Executable')
        file_entries.append('# Queue job')
        file_entries.append('queue')

    ofile = open( output_file, 'w' )

    for line in file_entries :
        ofile.write(  line + '\n' )

    ofile.close()

def wait_for_jobs( job_tag ) :

    while 1 :
        time.sleep(20)
        status = subprocess.Popen( ['condor_q'], stdout=subprocess.PIPE).communicate()[0]

        n_limits = 0

        for line in status.split('\n') :
            if line.count(job_tag ) :
                n_limits += 1

        if n_limits == 0 :
            return
        else :
            print '%d Jobs still running' %n_limits



main()