def config_samples(samples) :

    import ROOT

    samples.AddSample('SingleMuon'                       , path='SingleMuon'    ,  isActive=False, isData = True)
    samples.AddSample('SingleElectron'                       , path='SingleElectron'    ,  isActive=False, isData = True)

    samples.AddSample('DYJetsToLL_M-50',
                      path='DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
		              #path='DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('DYJetsToLL_M-50-amcatnloFXFXPhOlap',
                      path='DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8PhOlap',
                      isActive=False, useXSFile=True , XSName = 'DYJetsToLL_M-50-amcatnloFXFX')

    samples.AddSample('DYJetsToLL_M-50-amcatnloFXFX',
                      path='DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('ZGTo2LG',
                      path='ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('TTJets_DiLept',
                      #path='TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      path='TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('TTJets_SingleLeptFromTbar',
                      #path='TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      path='TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('TTJets_SingleLeptFromT',
                      #path='TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      path='TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('TTGJets',
                      path='TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('WGToLNuG-amcatnloFXFX',
                      path='WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kOrange )

    samples.AddSample('WGToLNuG-madgraphMLM',
                      path='WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kOrange )

    samples.AddSample('WGToLNuG_PtG-130-amcatnloFXFX',
                      path='WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kViolet )

    samples.AddSample('WGToLNuG_PtG-130-madgraphMLM',
                      path='WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kViolet )

    samples.AddSample('WGToLNuG_PtG-500-amcatnloFXFX',
                      path='WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kCyan   )

    samples.AddSample('WGToLNuG_PtG-500-madgraphMLM',
                      path='WGToLNuG_PtG-500_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kCyan   )

    samples.AddSample('WGToLNuG-amcatnloFXFXPhCut',
                      path='WGToLNuG_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutMax',
                      #path='WGToLNuG_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutMax',
                      isActive=False, useXSFile=True, plotColor=ROOT.kOrange, XSName='WGToLNuG-amcatnloFXFX')

    samples.AddSample('WGToLNuG_PtG-130-amcatnloFXFXPhCut',
                      path='WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutRange',
                      #path='WGToLNuG_PtG-130_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutMaxPhCutMin',
                      isActive=False, useXSFile=True, plotColor=ROOT.kViolet, XSName='WGToLNuG_PtG-130-amcatnloFXFX' )

    samples.AddSample('WGToLNuG_PtG-500-amcatnloFXFXPhCut',
                      path='WGToLNuG_PtG-500_TuneCP5_13TeV-amcatnloFXFX-pythia8PhCutMin',
                      isActive=False, useXSFile=True, plotColor=ROOT.kCyan, XSName='WGToLNuG_PtG-500-amcatnloFXFX'   )

    samples.AddSample('WGToLNuG-madgraphMLMPhCut',
                      path='WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMax',
                      #path='WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMax',
                      isActive=False, useXSFile=True, plotColor=ROOT.kOrange, XSName='WGToLNuG-madgraphMLM' )

    samples.AddSample('WGToLNuG_PtG-130-madgraphMLMPhCut',
                      path='WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMaxPhCutMin',
                      #path='WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMaxPhCutMin',
                      isActive=False, useXSFile=True, plotColor=ROOT.kViolet, XSName='WGToLNuG_PtG-130-madgraphMLM' )

    samples.AddSample('WGToLNuG_PtG-500-madgraphMLMPhCut',
                      path='WGToLNuG_PtG-500_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMin',
                      isActive=False, useXSFile=True, plotColor=ROOT.kCyan , XSName='WGToLNuG_PtG-500-madgraphMLM'  )

    samples.AddSample('WGToLNuG-madgraphMLMMTResCut',
                      path='WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8',
                      #path='WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMax',
                      isActive=False, useXSFile=True, plotColor=ROOT.kOrange, XSName='WGToLNuG-madgraphMLM' )

    samples.AddSample('WGToLNuG_PtG-130-madgraphMLMMTResCut',
                      path='WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8',
                      #path='WGToLNuG_PtG-130_TuneCP5_13TeV-madgraphMLM-pythia8PhCutMaxPhCutMin',
                      isActive=False, useXSFile=True, plotColor=ROOT.kViolet, XSName='WGToLNuG_PtG-130-madgraphMLM' )

    samples.AddSample('WGToLNuG_PtG-500-madgraphMLMMTResCut',
                      path='WGToLNuG_PtG-500_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True, plotColor=ROOT.kCyan , XSName='WGToLNuG_PtG-500-madgraphMLM'  )


    samples.AddSample('WJetsToLNu-madgraphMLM',
                      path='WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('WJetsToLNu-madgraphMLMPhOlap',
                      path='WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, useXSFile=True )

    samples.AddSample('WJetsToLNu-amcatnloFXFX',
                      path='WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8PhOlap',
                      isActive=False, useXSFile=True )

    samples.AddSample('WWG',
                      path='WWG_TuneCP5_13TeV-amcatnlo-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('tW_top',
                      path='ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('tW_antitop',
                      path='ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('DiPhoton',
                      path='DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8',
                      isActive=False, useXSFile=True )

    samples.AddSample('WJetsToLNuTrueHTOlap',
                      path='WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8TrueHTOlapPhOlap',
                      isActive=False, plotColor=ROOT.kGreen-5, useXSFile=True, XSName='WJetsToLNu-madgraphMLM')

    samples.AddSample('WJetsToLNu_HT-100To200',
                      path='WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kGreen , useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-200To400',
                      path='WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kCyan  , useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-400To600',
                      path='WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kViolet, useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-600To800',
                      path='WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kOrange, useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-800To1200',
                      path='WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kSpring, useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-1200To2500',
                      path='WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kGray  , useXSFile=True )

    samples.AddSample('WJetsToLNu_HT-2500ToInf',
                      path='WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8PhOlap',
                      isActive=False, plotColor=ROOT.kRed+6  , useXSFile=True )

    samples.AddSample('WJetsToLNu_Pt-0To50',
                      path='WJetsToLNu_Wpt-0To50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kGreen-5, useXSFile=True )
    samples.AddSample('WJetsToLNu_Pt-50To100',
                      path='WJetsToLNu_Wpt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kGreen, useXSFile=True )
    samples.AddSample('WJetsToLNu_Pt-100To250',
                      path='WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kCyan, useXSFile=True )
    samples.AddSample('WJetsToLNu_Pt-250To400',
                      path='WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kViolet, useXSFile=True )
    samples.AddSample('WJetsToLNu_Pt-400To600',
                      path='WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kOrange, useXSFile=True )
    samples.AddSample('WJetsToLNu_Pt-600ToInf',
                      path='WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kSpring, useXSFile=True )
    samples.AddSample('WToLNu_0J',
                      path='WToLNu_0J_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kGray, useXSFile=True )
    samples.AddSample('WToLNu_1J',
                      path='WToLNu_1J_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kRed+2, useXSFile=True )
    samples.AddSample('WToLNu_2J',
                      path='WToLNu_2J_13TeV-amcatnloFXFX-pythia8',
                      isActive=False, plotColor=ROOT.kPink, useXSFile=True )

    samples.AddSample('GJets_HT-40To100' , path='GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8', isActive=False, useXSFile=True)
    samples.AddSample('GJets_HT-100To200', path='GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', isActive=False, useXSFile=True)
    samples.AddSample('GJets_HT-200To400', path='GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', isActive=False, useXSFile=True)
    samples.AddSample('GJets_HT-400To600', path='GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', isActive=False, useXSFile=True)
    samples.AddSample('GJets_HT-600ToInf', path='GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', isActive=False, useXSFile=True)

    samples.AddSample('MadGraphResonanceMass200_width0p01', path='MadGraphChargedResonance_WGToLNuG_M200_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kCyan, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 200 GeV', XSName='ResonanceMass200')
    samples.AddSample('MadGraphResonanceMass200_width5', path='MadGraphChargedResonance_WGToLNuG_M200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 200 GeV', XSName='ResonanceMass200')
    samples.AddSample('MadGraphResonanceMass250_width0p01', path='MadGraphChargedResonance_WGToLNuG_M250_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 250 GeV', XSName='ResonanceMass250')
    samples.AddSample('MadGraphResonanceMass250_width5', path='MadGraphChargedResonance_WGToLNuG_M250_width5', isActive=True, isSignal=True, useXSFile=True, plotColor=ROOT.kPink-1, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 250 GeV', XSName='ResonanceMass250') #TODO: Active signal
    samples.AddSample('MadGraphResonanceMass300_width0p01', path='MadGraphChargedResonance_WGToLNuG_M300_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = 'M(#Phi^{#pm}) = 300 GeV', XSName='ResonanceMass300') #
    samples.AddSample('MadGraphResonanceMass300_width5', path='MadGraphChargedResonance_WGToLNuG_M300_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 300 GeV', XSName='ResonanceMass300')
    samples.AddSample('MadGraphResonanceMass350_width0p01', path='MadGraphChargedResonance_WGToLNuG_M350_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 350 GeV', XSName='ResonanceMass350')
    samples.AddSample('MadGraphResonanceMass350_width5', path='MadGraphChargedResonance_WGToLNuG_M350_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 350 GeV', XSName='ResonanceMass350')
    samples.AddSample('MadGraphResonanceMass400_width0p01', path='MadGraphChargedResonance_WGToLNuG_M400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kBlack, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 400 GeV', XSName='ResonanceMass400')
    samples.AddSample('MadGraphResonanceMass400_width5', path='MadGraphChargedResonance_WGToLNuG_M400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 400 GeV', XSName='ResonanceMass400')
    samples.AddSample('MadGraphResonanceMass450_width0p01', path='MadGraphChargedResonance_WGToLNuG_M450_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 450 GeV', XSName='ResonanceMass450')
    samples.AddSample('MadGraphResonanceMass450_width5', path='MadGraphChargedResonance_WGToLNuG_M450_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kBlue, legend_name = 'M(#Phi^{#pm}) = 450 GeV', XSName='ResonanceMass450') #
    samples.AddSample('MadGraphResonanceMass500_width0p01', path='MadGraphChargedResonance_WGToLNuG_M500_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 500 GeV', XSName='ResonanceMass500')
    samples.AddSample('MadGraphResonanceMass500_width5', path='MadGraphChargedResonance_WGToLNuG_M500_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 500 GeV', XSName='ResonanceMass500')
    samples.AddSample('MadGraphResonanceMass600_width0p01', path='MadGraphChargedResonance_WGToLNuG_M600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 600 GeV', XSName='ResonanceMass600')
    samples.AddSample('MadGraphResonanceMass600_width5', path='MadGraphChargedResonance_WGToLNuG_M600_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 600 GeV', XSName='ResonanceMass600')
    samples.AddSample('MadGraphResonanceMass700_width0p01', path='MadGraphChargedResonance_WGToLNuG_M700_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 700 GeV', XSName='ResonanceMass700')
    samples.AddSample('MadGraphResonanceMass700_width5', path='MadGraphChargedResonance_WGToLNuG_M700_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 700 GeV', XSName='ResonanceMass700')
    samples.AddSample('MadGraphResonanceMass800_width0p01', path='MadGraphChargedResonance_WGToLNuG_M800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kMagenta, legend_name = 'M(#Phi^{#pm}) = 800 GeV', XSName='ResonanceMass800') #
    samples.AddSample('MadGraphResonanceMass800_width5', path='MadGraphChargedResonance_WGToLNuG_M800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 800 GeV', XSName='ResonanceMass800')
    samples.AddSample('MadGraphResonanceMass900_width0p01', path='MadGraphChargedResonance_WGToLNuG_M900_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 900 GeV', XSName='ResonanceMass900')
    samples.AddSample('MadGraphResonanceMass900_width5', path='MadGraphChargedResonance_WGToLNuG_M900_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 900 GeV', XSName='ResonanceMass900')
    samples.AddSample('MadGraphResonanceMass1000_width0p01', path='MadGraphChargedResonance_WGToLNuG_M1000_width0p01', isActive=True, isSignal=True, useXSFile=True, plotColor=ROOT.kPink+10, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1000 GeV', XSName='ResonanceMass1000') #TODO: Active signal
    samples.AddSample('MadGraphResonanceMass1000_width5', path='MadGraphChargedResonance_WGToLNuG_M1000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1000 GeV', XSName='ResonanceMass1000')
    samples.AddSample('MadGraphResonanceMass1200_width0p01', path='MadGraphChargedResonance_WGToLNuG_M1200_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1200 GeV', XSName='ResonanceMass1200')
    samples.AddSample('MadGraphResonanceMass1200_width5', path='MadGraphChargedResonance_WGToLNuG_M1200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1200 GeV', XSName='ResonanceMass1200')
    samples.AddSample('MadGraphResonanceMass1400_width0p01', path='MadGraphChargedResonance_WGToLNuG_M1400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1400 GeV', XSName='ResonanceMass1400')
    samples.AddSample('MadGraphResonanceMass1400_width5', path='MadGraphChargedResonance_WGToLNuG_M1400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1400 GeV', XSName='ResonanceMass1400')
    samples.AddSample('MadGraphResonanceMass1600_width0p01', path='MadGraphChargedResonance_WGToLNuG_M1600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1600 GeV', XSName='ResonanceMass1600')
    samples.AddSample('MadGraphResonanceMass1600_width5', path='MadGraphChargedResonance_WGToLNuG_M1600_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1600 GeV', XSName='ResonanceMass1600')
    samples.AddSample('MadGraphResonanceMass1800_width0p01', path='MadGraphChargedResonance_WGToLNuG_M1800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1800 GeV', XSName='ResonanceMass1800')
    samples.AddSample('MadGraphResonanceMass1800_width5', path='MadGraphChargedResonance_WGToLNuG_M1800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1800 GeV', XSName='ResonanceMass1800')
    samples.AddSample('MadGraphResonanceMass2000_width0p01', path='MadGraphChargedResonance_WGToLNuG_M2000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kGreen, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2000 GeV', XSName='ResonanceMass2000')
    samples.AddSample('MadGraphResonanceMass2000_width5', path='MadGraphChargedResonance_WGToLNuG_M2000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2000 GeV', XSName='ResonanceMass2000')
    samples.AddSample('MadGraphResonanceMass2200_width0p01', path='MadGraphChargedResonance_WGToLNuG_M2200_width0p01', isActive=True, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2200 GeV', XSName='ResonanceMass2200')#TODO: Active signal
    samples.AddSample('MadGraphResonanceMass2200_width5', path='MadGraphChargedResonance_WGToLNuG_M2200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2200 GeV', XSName='ResonanceMass2200')
    samples.AddSample('MadGraphResonanceMass2400_width0p01', path='MadGraphChargedResonance_WGToLNuG_M2400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2400 GeV', XSName='ResonanceMass2400')
    samples.AddSample('MadGraphResonanceMass2400_width5', path='MadGraphChargedResonance_WGToLNuG_M2400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2400 GeV', XSName='ResonanceMass2400')
    samples.AddSample('MadGraphResonanceMass2600_width0p01', path='MadGraphChargedResonance_WGToLNuG_M2600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2600 GeV', XSName='ResonanceMass2600')
    samples.AddSample('MadGraphResonanceMass2800_width0p01', path='MadGraphChargedResonance_WGToLNuG_M2800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2800 GeV', XSName='ResonanceMass2800')
    samples.AddSample('MadGraphResonanceMass2800_width5', path='MadGraphChargedResonance_WGToLNuG_M2800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2800 GeV', XSName='ResonanceMass2800')
    samples.AddSample('MadGraphResonanceMass3000_width0p01', path='MadGraphChargedResonance_WGToLNuG_M3000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3000 GeV', XSName='ResonanceMass3000')
    samples.AddSample('MadGraphResonanceMass3500_width0p01', path='MadGraphChargedResonance_WGToLNuG_M3500_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3500 GeV', XSName='ResonanceMass3500')
    samples.AddSample('MadGraphResonanceMass3500_width5', path='MadGraphChargedResonance_WGToLNuG_M3500_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3500 GeV', XSName='ResonanceMass3500')
    samples.AddSample('MadGraphResonanceMass4000_width0p01', path='MadGraphChargedResonance_WGToLNuG_M4000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 4000 GeV', XSName='ResonanceMass4000')
    samples.AddSample('MadGraphResonanceMass4000_width5', path='MadGraphChargedResonance_WGToLNuG_M4000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 4000 GeV', XSName='ResonanceMass4000')

    samples.AddSample('PythiaResonanceMass200_width0p01', path='PythiaChargedResonance_WGToLNuG_M200_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kCyan, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 200 GeV', XSName='ResonanceMass200')
    samples.AddSample('PythiaResonanceMass200_width5', path='PythiaChargedResonance_WGToLNuG_M200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 200 GeV', XSName='ResonanceMass200')
    samples.AddSample('PythiaResonanceMass250_width0p01', path='PythiaChargedResonance_WGToLNuG_M250_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 250 GeV', XSName='ResonanceMass250')
    samples.AddSample('PythiaResonanceMass250_width5', path='PythiaChargedResonance_WGToLNuG_M250_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 250 GeV', XSName='ResonanceMass250')
    samples.AddSample('PythiaResonanceMass300_width0p01', path='PythiaChargedResonance_WGToLNuG_M300_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 300 GeV', XSName='ResonanceMass300')
    samples.AddSample('PythiaResonanceMass300_width5', path='PythiaChargedResonance_WGToLNuG_M300_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 300 GeV', XSName='ResonanceMass300')
    samples.AddSample('PythiaResonanceMass350_width0p01', path='PythiaChargedResonance_WGToLNuG_M350_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 350 GeV', XSName='ResonanceMass350')
    samples.AddSample('PythiaResonanceMass350_width5', path='PythiaChargedResonance_WGToLNuG_M350_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 350 GeV', XSName='ResonanceMass350')
    samples.AddSample('PythiaResonanceMass400_width0p01', path='PythiaChargedResonance_WGToLNuG_M400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kBlack, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 400 GeV', XSName='ResonanceMass400')
    samples.AddSample('PythiaResonanceMass400_width5', path='PythiaChargedResonance_WGToLNuG_M400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 400 GeV', XSName='ResonanceMass400')
    samples.AddSample('PythiaResonanceMass450_width0p01', path='PythiaChargedResonance_WGToLNuG_M450_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 450 GeV', XSName='ResonanceMass450')
    samples.AddSample('PythiaResonanceMass450_width5', path='PythiaChargedResonance_WGToLNuG_M450_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 450 GeV', XSName='ResonanceMass450')
    samples.AddSample('PythiaResonanceMass500_width0p01', path='PythiaChargedResonance_WGToLNuG_M500_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 500 GeV', XSName='ResonanceMass500')
    samples.AddSample('PythiaResonanceMass500_width5', path='PythiaChargedResonance_WGToLNuG_M500_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 500 GeV', XSName='ResonanceMass500')
    samples.AddSample('PythiaResonanceMass600_width0p01', path='PythiaChargedResonance_WGToLNuG_M600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 600 GeV', XSName='ResonanceMass600')
    samples.AddSample('PythiaResonanceMass600_width5', path='PythiaChargedResonance_WGToLNuG_M600_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 600 GeV', XSName='ResonanceMass600')
    samples.AddSample('PythiaResonanceMass700_width0p01', path='PythiaChargedResonance_WGToLNuG_M700_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 700 GeV', XSName='ResonanceMass700')
    samples.AddSample('PythiaResonanceMass700_width5', path='PythiaChargedResonance_WGToLNuG_M700_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 700 GeV', XSName='ResonanceMass700')
    samples.AddSample('PythiaResonanceMass800_width0p01', path='PythiaChargedResonance_WGToLNuG_M800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kMagenta, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 800 GeV', XSName='ResonanceMass800')
    samples.AddSample('PythiaResonanceMass800_width5', path='PythiaChargedResonance_WGToLNuG_M800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 800 GeV', XSName='ResonanceMass800')
    samples.AddSample('PythiaResonanceMass900_width0p01', path='PythiaChargedResonance_WGToLNuG_M900_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 900 GeV', XSName='ResonanceMass900')
    samples.AddSample('PythiaResonanceMass900_width5', path='PythiaChargedResonance_WGToLNuG_M900_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 900 GeV', XSName='ResonanceMass900')
    samples.AddSample('PythiaResonanceMass1000_width0p01', path='PythiaChargedResonance_WGToLNuG_M1000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1000 GeV', XSName='ResonanceMass1000')
    samples.AddSample('PythiaResonanceMass1000_width5', path='PythiaChargedResonance_WGToLNuG_M1000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1000 GeV', XSName='ResonanceMass1000')
    samples.AddSample('PythiaResonanceMass1200_width0p01', path='PythiaChargedResonance_WGToLNuG_M1200_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1200 GeV', XSName='ResonanceMass1200')
    samples.AddSample('PythiaResonanceMass1200_width5', path='PythiaChargedResonance_WGToLNuG_M1200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1200 GeV', XSName='ResonanceMass1200')
    samples.AddSample('PythiaResonanceMass1400_width0p01', path='PythiaChargedResonance_WGToLNuG_M1400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1400 GeV', XSName='ResonanceMass1400')
    samples.AddSample('PythiaResonanceMass1400_width5', path='PythiaChargedResonance_WGToLNuG_M1400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1400 GeV', XSName='ResonanceMass1400')
    samples.AddSample('PythiaResonanceMass1600_width0p01', path='PythiaChargedResonance_WGToLNuG_M1600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1600 GeV', XSName='ResonanceMass1600')
    samples.AddSample('PythiaResonanceMass1600_width5', path='PythiaChargedResonance_WGToLNuG_M1600_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1600 GeV', XSName='ResonanceMass1600')
    samples.AddSample('PythiaResonanceMass1800_width0p01', path='PythiaChargedResonance_WGToLNuG_M1800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1800 GeV', XSName='ResonanceMass1800')
    samples.AddSample('PythiaResonanceMass1800_width5', path='PythiaChargedResonance_WGToLNuG_M1800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 1800 GeV', XSName='ResonanceMass1800')
    samples.AddSample('PythiaResonanceMass2000_width0p01', path='PythiaChargedResonance_WGToLNuG_M2000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kGreen, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2000 GeV', XSName='ResonanceMass2000')
    samples.AddSample('PythiaResonanceMass2000_width5', path='PythiaChargedResonance_WGToLNuG_M2000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2000 GeV', XSName='ResonanceMass2000')
    samples.AddSample('PythiaResonanceMass2200_width0p01', path='PythiaChargedResonance_WGToLNuG_M2200_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2200 GeV', XSName='ResonanceMass2200')
    samples.AddSample('PythiaResonanceMass2200_width5', path='PythiaChargedResonance_WGToLNuG_M2200_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2200 GeV', XSName='ResonanceMass2200')
    samples.AddSample('PythiaResonanceMass2400_width0p01', path='PythiaChargedResonance_WGToLNuG_M2400_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2400 GeV', XSName='ResonanceMass2400')
    samples.AddSample('PythiaResonanceMass2400_width5', path='PythiaChargedResonance_WGToLNuG_M2400_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2400 GeV', XSName='ResonanceMass2400')
    samples.AddSample('PythiaResonanceMass2600_width0p01', path='PythiaChargedResonance_WGToLNuG_M2600_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2600 GeV', XSName='ResonanceMass2600')
    samples.AddSample('PythiaResonanceMass2800_width0p01', path='PythiaChargedResonance_WGToLNuG_M2800_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2800 GeV', XSName='ResonanceMass2800')
    samples.AddSample('PythiaResonanceMass2800_width5', path='PythiaChargedResonance_WGToLNuG_M2800_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 2800 GeV', XSName='ResonanceMass2800')
    samples.AddSample('PythiaResonanceMass3000_width0p01', path='PythiaChargedResonance_WGToLNuG_M3000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3000 GeV', XSName='ResonanceMass3000')
    samples.AddSample('PythiaResonanceMass3500_width0p01', path='PythiaChargedResonance_WGToLNuG_M3500_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3500 GeV', XSName='ResonanceMass3500')
    samples.AddSample('PythiaResonanceMass3500_width5', path='PythiaChargedResonance_WGToLNuG_M3500_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 3500 GeV', XSName='ResonanceMass3500')
    samples.AddSample('PythiaResonanceMass4000_width0p01', path='PythiaChargedResonance_WGToLNuG_M4000_width0p01', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 4000 GeV', XSName='ResonanceMass4000')
    samples.AddSample('PythiaResonanceMass4000_width5', path='PythiaChargedResonance_WGToLNuG_M4000_width5', isActive=False, isSignal=True, useXSFile=True, plotColor=ROOT.kRed, legend_name = '#Phi^{#pm} #rightarrow W^{#pm}#gamma, M = 4000 GeV', XSName='ResonanceMass4000')


    samples.AddSampleGroup( 'Data', legend_name='Data',
                            input_samples = [
                                             'SingleMuon',
                                             'SingleElectron',
                                            ],
                           plotColor=ROOT.kBlack,
                           isData=True,
                          )


    samples.AddSampleGroup(  'WGamma', legend_name='W#gamma',
                           #input_samples = ['WGToLNuG-amcatnloFXFXPhCut', 'WGToLNuG_PtG-130-amcatnloFXFXPhCut','WGToLNuG_PtG-500-amcatnloFXFXPhCut' ],
                           input_samples = ['WGToLNuG-amcatnloFXFX'],
                           #input_samples = ['WGToLNuG-amcatnloFXFXPhCut', 'WGToLNuG_PtG-130-amcatnloFXFXPhCut','WGToLNuG_PtG-500-amcatnloFXFXPhCut' ],
                           #input_samples = ['WGToLNuG_PtG-130-amcatnloFXFXPhCut','WGToLNuG_PtG-500-amcatnloFXFXPhCut' ],
                           plotColor = ROOT.kRed-2,
                           isActive=True,
                          )

    samples.AddSampleGroup( 'GammaGamma', legend_name='#gamma#gamma',
                           input_samples = [
                                           'DiPhoton',
                           ],
                           plotColor = ROOT.kYellow,
                          )

    samples.AddSampleGroup(  'Zgamma', legend_name='Z#gamma',
                           input_samples = ['ZGTo2LG'],
                           plotColor = ROOT.kRed-8,
                           isActive=False
                          )

    samples.AddSampleGroup(  'Z+jetsLO', legend_name='Z+JetsLO',
                           input_samples = ['DYJetsToLL_M-50'],
                           plotColor = ROOT.kCyan-2,
                           isActive=False,
                          )

    samples.AddSampleGroup(  'Z+jets', legend_name='Z+Jets',
                           #input_samples = ['DYJetsToLL_M-50-amcatnloFXFXPhOlap'],
                           input_samples = ['DYJetsToLL_M-50-amcatnloFXFX'],
                           plotColor = ROOT.kCyan-5,
                          )




    samples.AddSampleGroup(  'WGammaLO', legend_name='W#gamma LO',
#                           #input_samples = ['WGToLNuG-madgraphMLMPhCut', 'WGToLNuG_PtG-130-madgraphMLMPhCut','WGToLNuG_PtG-500-madgraphMLMPhCut' ],
                           input_samples = ['WGToLNuG-madgraphMLMMTResCut', 'WGToLNuG_PtG-130-madgraphMLMMTResCut','WGToLNuG_PtG-500-madgraphMLMMTResCut' ],
#                           #input_samples = ['WGToLNuG_PtG-130-madgraphMLMPhCut','WGToLNuG_PtG-500-madgraphMLMPhCut' ],
                           plotColor = ROOT.kRed-2,
                           isActive=False,
                          )

    samples.AddSampleGroup(  'Wjets', legend_name='W+Jets',
                           #input_samples = ['WJetsToLNu-madgraphMLMPhOlap'],
                           input_samples = [
                                            #'WJetsToLNuTrueHTOlap',
                                            'WJetsToLNu_HT-100To200',
                                            'WJetsToLNu_HT-200To400',
                                            'WJetsToLNu_HT-400To600',
                                            'WJetsToLNu_HT-600To800',
                                            'WJetsToLNu_HT-800To1200',
                                            'WJetsToLNu_HT-1200To2500',
                                            'WJetsToLNu_HT-2500ToInf',
                           ],
                           plotColor = ROOT.kBlue-2,
                           #isActive=False,
                          )
##>>
    samples.AddSampleGroup( 'TTG', legend_name='t#bar{t}#gamma',
                           input_samples = ['TTGJets'],
                           plotColor = ROOT.kAzure+1,
                           #isActive=False,
                          )

#    samples.AddSampleGroup( 'WjetsSMPIncl', legend_name='W+Jets',
#                            input_samples = ['WJetsToLNu-amcatnloFXFX'],
#                            plotColor = ROOT.kBlue-2,
#                            isActive=False
#                            )
#
#    samples.AddSampleGroup( 'WjetsSMPPt', legend_name='W+Jets',
#                            input_samples = [
#                            'WJetsToLNu_Pt-0To50',
#                            'WJetsToLNu_Pt-50To100',
#                            'WJetsToLNu_Pt-100To250',
#                            'WJetsToLNu_Pt-250To400',
#                            'WJetsToLNu_Pt-400To600',
#                            'WJetsToLNu_Pt-600ToInf',
#                            ],
#                            plotColor = ROOT.kBlue-2,
#                            )
#
#    samples.AddSampleGroup( 'WjetsSMPJet', legend_name='W+Jets',
#                            input_samples = [
#                            'WToLNu_0J',
#                            'WToLNu_1J',
#                            'WToLNu_2J',
#                            ],
#                            plotColor = ROOT.kBlue-2,
#                            )


    samples.AddSampleGroup( 'GJets', legend_name='#gamma + jets',
                           input_samples = [
                                           'GJets_HT-100To200',
                                           'GJets_HT-200To400',
                                           'GJets_HT-400To600',
                                           'GJets_HT-40To100' ,
                                           'GJets_HT-600ToInf',
                           ],
                           plotColor = ROOT.kOrange,
                           #isActive=False,
                          )




    samples.AddSampleGroup( 'TTbar_DiLep', legend_name='t#bar{t} dileptonic',
                           input_samples = ['TTJets_DiLept'],
                           plotColor = ROOT.kMagenta+2,
                           isActive=False,
                          )

    samples.AddSampleGroup( 'TTbar_SingleLep', legend_name='t#bar{t} semileptonic',
                           input_samples = ['TTJets_SingleLeptFromTbar', 'TTJets_SingleLeptFromT'],
                           plotColor = ROOT.kGreen+2,
                           isActive=False,
                          )
#<<#

    samples.AddSampleGroup( 'AllTop', legend_name='t#bar{t}',
                           input_samples = ['TTbar_DiLep', 'TTbar_SingleLep'],
                           plotColor = ROOT.kGreen+3,
                           isActive=True,
                          )

    samples.AddSampleGroup( 'TopW', legend_name='tW',
                           input_samples = ['tW_top','tW_antitop'],
                           plotColor = ROOT.kOrange+3,
                           isActive=True,
                          )

    samples.AddSampleGroup( 'Others', legend_name='Others',
                           input_samples = ['TTbar_DiLep', 'TTbar_SingleLep','TTG','GJets','Wjets'],
                           plotColor = ROOT.kGray,
                           isActive=False,
                          )

    samples.AddSampleGroup( 'MCBackground', legend_name='MC Background',
                           input_samples = ['WGamma', 'Wjets', 'TTbar_DiLep', 'TTbar_SingleLep'],
                           isActive=False,
                          )
    samples.AddSampleGroup( 'MCBackgroundLO', legend_name='MC Background',
                           input_samples = ['WGammaLO', 'Wjets', 'TTbar_DiLep', 'TTbar_SingleLep'],
                           isActive=False,
                          )
    samples.AddSampleGroup( 'JetBackground', legend_name='Jet Background',
                           input_samples = ['Wjets', 'TTbar_SingleLep'],
                           isActive=False,
                          )
    samples.AddSampleGroup( 'EleFakeBackground',
                           input_samples = ['Z+jets', 'Zgamma', 'TTbar_DiLep'],
                           isActive=False,
                          )

def print_examples() :
    pass

