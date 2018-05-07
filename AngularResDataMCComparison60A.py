from ROOT import *
import os
import math
import argparse


# Get BeamComposition: percentage of pions, muons and electrons in a 60A beam configuration
#                       The beam at 60A is 


pionInBeam60A = 0.688  # 68.8% pions
#muonInBeam60A = 0.046  #  4.6% muons
#elecInBeam60A = 0.266  # 26.6% electrons


# Electron to Pion and Muon to Pion Ratio
#elecScale = elecInBeam60A/pionInBeam60A
#muonScale = muonInBeam60A/pionInBeam60A

# Get Files' names
pionMC_FileName = "/Volumes/Seagate/Elena/TPC/MC60A_Pions.root"
#muonMC_FileName = "/Volumes/Seagate/Elena/TPC/MC60A_Muon.root"
#elecMC_FileName = "/Volumes/Seagate/Elena/TPC/MC60A_Electron.root"
data_FileName   = "/Volumes/Seagate/Elena/TPC/Data60A.root"

pionMC_File   = TFile.Open(pionMC_FileName)
#muonMC_File   = TFile.Open(muonMC_FileName)
#elecMC_File   = TFile.Open(elecMC_FileName)
data_File     = TFile.Open(data_FileName)

# Get Interacting and Incident plots
treeName = "TrackingResoultion/trackResTree"
pionMC_Tree  = pionMC_File.Get(treeName)
#muonMC_Tree  = muonMC_File.Get(treeName)
#elecMC_Tree  = elecMC_File.Get(treeName)
data_Tree    = data_File.Get(treeName)


cTracking = TCanvas("cTracking" ,"cTracking" ,200 ,10 ,1200 ,600)
cTracking.Divide(2,1)
p1 = cTracking.cd(1)
p1.SetGrid()
pionMC_Tree.Draw("chi2_Full>>hChi2_Full_pionMC(200,0,10)")
#muonMC_Tree.Draw("chi2_Full>>hChi2_Full_muonMC(200,0,10)")
#elecMC_Tree.Draw("chi2_Full>>hChi2_Full_elecMC(200,0,10)")
data_Tree.Draw("chi2_Full>>hChi2_Full_data(200,0,10)")

#hChi2_Full_elecMC.Scale(elecScale)
#hChi2_Full_muonMC.Scale(muonScale)
#hChi2_Full_pionMC.Add(hChi2_Full_elecMC)
#hChi2_Full_pionMC.Add(hChi2_Full_muonMC)
hChi2_Full_pionMC.SetLineColor(kRed)
hChi2_Full_pionMC.SetLineWidth(2)
hChi2_Full_pionMC.Scale(1./hChi2_Full_pionMC.Integral())

hChi2_Full_data.Scale(1./hChi2_Full_data.Integral())
hChi2_Full_data.SetMarkerStyle(21)
hChi2_Full_data.SetMarkerSize(0.5)
hChi2_Full_data.SetLineColor(kBlack)

hChi2_Full_pionMC.SetTitle("#Chi^{2} Tracking; #Chi^{2}; Area Normalized Entries")
hChi2_Full_pionMC.Draw("histo")
hChi2_Full_data.Draw("pesames")
cTracking.Update()



p2 = cTracking.cd(2)
p2.SetGrid()
pionMC_Tree.Draw("alpha_1Half+alpha_2Half>>AngularResolutionMC(200,0,1)")
#muonMC_Tree.Draw("alpha_1Half+alpha_2Half>>hAngle_Full_muonMC(200,0,1)")
#elecMC_Tree.Draw("alpha_1Half+alpha_2Half>>hAngle_Full_elecMC(200,0,1)")
data_Tree  .Draw("alpha_1Half+alpha_2Half>>AngularResolutionData(200,0,1)")

#hAngle_Full_elecMC.Scale(elecScale)
#hAngle_Full_muonMC.Scale(muonScale)
#AngularResolutionMC.Add(hAngle_Full_elecMC)
#AngularResolutionMC.Add(hAngle_Full_muonMC)
AngularResolutionMC.SetLineColor(kRed)
AngularResolutionMC.SetLineWidth(2)
AngularResolutionMC.Scale(1./AngularResolutionMC.Integral())

AngularResolutionData.Scale(1./AngularResolutionData.Integral())
AngularResolutionData.SetMarkerStyle(21)
AngularResolutionData.SetMarkerSize(0.5)
AngularResolutionData.SetLineColor(kBlack)

AngularResolutionMC.SetTitle("Angular Resolution; #alpha [rad]; Area Normalized Entries")
AngularResolutionMC.Draw("histos")
AngularResolutionData.Draw("pesames")
cTracking.Update()




cTrackingDeg = TCanvas("cTrackingDeg" ,"cTracking" ,200 ,10 ,600 ,600)
cTrackingDeg.SetGrid()
pionMC_Tree.Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionMC(100,0,20)")
#muonMC_Tree.Draw("57.2958*(alpha_1Half+alpha_2Half)>>hDegAngle_Full_muonMC(100,0,20)")
#elecMC_Tree.Draw("57.2958*(alpha_1Half+alpha_2Half)>>hDegAngle_Full_elecMC(100,0,20)")
data_Tree  .Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionData(100,0,20)")

#hDegAngle_Full_elecMC.Scale(elecScale)
#hDegAngle_Full_muonMC.Scale(muonScale)
#DegAngularResolutionMC.Add(hDegAngle_Full_elecMC)
#DegAngularResolutionMC.Add(hDegAngle_Full_muonMC)
DegAngularResolutionMC.SetLineColor(kRed)
DegAngularResolutionMC.SetLineWidth(2)
DegAngularResolutionMC.Scale(1./DegAngularResolutionMC.Integral())

DegAngularResolutionData.Scale(1./DegAngularResolutionData.Integral())
DegAngularResolutionData.SetMarkerStyle(21)
DegAngularResolutionData.SetMarkerSize(0.5)
DegAngularResolutionData.SetLineColor(kBlack)

DegAngularResolutionMC.SetTitle("Angular Resolution; #alpha [Deg]; Area Normalized Entries")
DegAngularResolutionMC.Draw("histos")
DegAngularResolutionData.Draw("pesames")

cTrackingDeg.Update()


#for  entry in myTree:
'''
cPion60A = TCanvas("cPion60A" ,"Plots Overlay" ,200 ,10 ,900 ,900)
cPion60A.Divide(2,1) 
p1 = cPion60A.cd(1)
p1.SetGrid()
pionContent_Int = pionMC_Int.Clone("pionContent_Int")
pionContent_Int.Sumw2()
pionContent_Int.Divide(totHisto_Int)
pionContent_Int.Draw("")
p2 = cPion60A.cd(2)
p2.SetGrid()
pionContent_Inc = pionMC_Inc.Clone("pionContent_Inc")
pionContent_Inc.Sumw2()
pionContent_Inc.Divide(totHisto_Inc)
pionContent_Inc.Draw("")
cPion60A.SetGrid()
cPion60A.Update()



nSpt_Full       = 384
 nSpt_1Half      = 190
 nSpt_2Half      = 190
 chi2_Full       = 0.62566
 chi2_1Half      = 0.232433
 chi2_2Half      = 0.39554
 delta_Alpha     = -0.00738096
 alpha_1Half     = 0.0227158
 alpha_2Half     = 0.0300968

# Let's assign a color scheme --> check color scheme is the same as G4Beamline
pionMC_Int.SetFillColor(9)
muonMC_Int.SetFillColor(41)
elecMC_Int.SetFillColor(40)    
pionMC_Inc.SetFillColor(9)    
muonMC_Inc.SetFillColor(41)
elecMC_Inc.SetFillColor(40)    

legend = TLegend(.54,.52,.84,.70);
legend.AddEntry(pionMC_Int,"MC 60A pions");
legend.AddEntry(muonMC_Int,"MC 60A muons");
legend.AddEntry(elecMC_Int,"MC 60A electrons");


#Scale according to beam composition, both interacting and incident plots
elecMC_Int.Scale(elecScale)
elecMC_Inc.Scale(elecScale)
muonMC_Int.Scale(muonScale)
muonMC_Inc.Scale(muonScale)

 


# Form staggered plots for incident
interactingStack60A = THStack("interactingStack60A", "Interacting Stack with Beam Weights; Interacting K.E. [MeV]; Entries per 50 MeV");
interactingStack60A.Add(muonMC_Int )
interactingStack60A.Add(elecMC_Int )
interactingStack60A.Add(pionMC_Int )

# Form staggered plots for incident
incidentStack60A = THStack("incidentStack60A", "Incident Stack with Beam Weights; Incident K.E. [MeV]; Entries per 50 MeV");
incidentStack60A.Add(muonMC_Inc )
incidentStack60A.Add(elecMC_Inc )
incidentStack60A.Add(pionMC_Inc )

# Staggered plots by hand
totHisto_Int = pionMC_Int.Clone("totHisto_Int")
totHisto_Inc = pionMC_Inc.Clone("totHisto_Inc")
for i in xrange(pionMC_Int.GetSize()):
    totHisto_Int.SetBinContent(i, muonMC_Int.GetBinContent(i)+elecMC_Int.GetBinContent(i)+ pionMC_Int.GetBinContent(i))
    totHisto_Inc.SetBinContent(i, muonMC_Inc.GetBinContent(i)+elecMC_Inc.GetBinContent(i)+ pionMC_Inc.GetBinContent(i))


#PionMuE Cross Section
cRecoPiMuEXS = TCanvas("cRecoPiMuEXS" ,"#pi/#mu/e Reconstructed Cross Section" ,200 ,10 ,900 ,900)
cRecoPiMuEXS.Divide(2,2) 
PiMuEXS = totHisto_Int.Clone("MC_PiMuERecoXS")
PiMuEXS.Sumw2()
PiMuEXS.Divide(totHisto_Inc)
PiMuEXS.Scale(101.10968) 
PiMuEXS.SetTitle("#pi/#mu/e MC Reconstructed Cross Section; K.E. [MeV]; Total Hadronic Cross Section per 50 MeV [barn]")
PiMuEXS.Draw("pe")

#PionOnly Cross Section
cRecoPionOnlyXS = TCanvas("cRecoPionOnlyXS" ,"#pi/#mu/e Reconstructed Cross Section" ,200 ,10 ,900 ,900)
cRecoPionOnlyXS.Divide(2,2) 
PionOnlyXS = pionMC_Int.Clone("MC_PionOnlyRecoXS")
PionOnlyXS.Sumw2()
PionOnlyXS.Divide(pionMC_Inc)
PionOnlyXS.Scale(101.10968) 
PionOnlyXS.SetTitle("#pi MC Reconstructed Cross Section; K.E. [MeV]; Total Hadronic Cross Section per 50 MeV [barn]")
PionOnlyXS.Draw("pe")


#PionContent
cPion60A = TCanvas("cPion60A" ,"Plots Overlay" ,200 ,10 ,900 ,900)
cPion60A.Divide(2,2) 
p1 = cPion60A.cd(1)
p1.SetGrid()
pionContent_Int = pionMC_Int.Clone("pionContent_Int")
pionContent_Int.Sumw2()
pionContent_Int.Divide(totHisto_Int)
pionContent_Int.Draw("")
p2 = cPion60A.cd(2)
p2.SetGrid()
pionContent_Inc = pionMC_Inc.Clone("pionContent_Inc")
pionContent_Inc.Sumw2()
pionContent_Inc.Divide(totHisto_Inc)
pionContent_Inc.Draw("")
cPion60A.SetGrid()
cPion60A.Update()


##Plot Staggered plots
p3 = cPion60A.cd(3)
p3.SetGrid()
interactingStack60A.Draw("histo")
legend.Draw("same")
p4 = cPion60A.cd(4)
p4.SetGrid()
incidentStack60A.Draw("histo")
legend.Draw("same")
cPion60A.Update()

outFile = TFile("BackGroundCorrectionPions60A.root","recreate")
outFile.cd()
pionContent_Int.Write("backgroundCorrection_Int",TObject.kWriteDelete)
pionContent_Inc.Write("backgroundCorrection_Inc",TObject.kWriteDelete)
PiMuEXS.Write()
PionOnlyXS.Write()
outFile.Write()
outFile.Close()



'''

raw_input()  



