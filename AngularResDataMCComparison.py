from ROOT import *
import os
import math
import argparse


gStyle.SetOptStat(1101);

# Get Files' names
pionMC_FileName     = "TrackingResolution_histoPionMC60A.root"
data_FileName       = "TrackingResolution_histoData60A.root"
pionMC_100AFileName = "/Volumes/Seagate/Elena/TPC/Pion100A_MC.root"
data_100AFileName   = "/Volumes/Seagate/Elena/TPC/Data100A.root"

pionMC_File       = TFile.Open(pionMC_FileName)
data_File         = TFile.Open(data_FileName)
pionMC100A_File   = TFile.Open(pionMC_100AFileName)
data100A_File     = TFile.Open(data_100AFileName)

# Get Interacting and Incident plots
#treeName = "TrackingResoultion/trackResTree"
treeName     = "TRes/trackResTree"
pionMC_Tree  = pionMC_File.Get(treeName)
data_Tree    = data_File.Get(treeName)

treeName100A     = "TrackingResoultion/trackResTree"
pionMC100A_Tree  = pionMC100A_File.Get(treeName100A)
data100A_Tree    = data100A_File.Get(treeName100A)

cTracking = TCanvas("cTracking" ,"cTracking" ,200 ,10 ,1200 ,600)
cTracking.Divide(2,1)
p1 = cTracking.cd(1)
p1.SetGrid()
pionMC_Tree.Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionMC(200,0,40)")
data_Tree  .Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionData(200,0,40)")
pionMC100A_Tree.Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionMC100A(200,0,40)")
data100A_Tree  .Draw("57.2958*(alpha_1Half+alpha_2Half)>>DegAngularResolutionData100A(200,0,40)")

DegAngularResolutionMC.Add(DegAngularResolutionMC100A)
DegAngularResolutionData.Add(DegAngularResolutionData100A)

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

legend = TLegend(.54,.52,.84,.70);
legend.AddEntry(DegAngularResolutionMC,"Pion Only MC");
legend.AddEntry(DegAngularResolutionData,"Data");
legend.Draw("same")
cTracking.Update()



p2 = cTracking.cd(2)
p2.SetGrid()
pionMC_Tree.Draw("alpha_1Half+alpha_2Half>>AngularResolutionMC(200,0,1)")
data_Tree  .Draw("alpha_1Half+alpha_2Half>>AngularResolutionData(200,0,1)")
pionMC100A_Tree.Draw("alpha_1Half+alpha_2Half>>AngularResolutionMC100A(200,0,1)")
data100A_Tree  .Draw("alpha_1Half+alpha_2Half>>AngularResolutionData100A(200,0,1)")

AngularResolutionMC.Add(AngularResolutionMC100A)
AngularResolutionData.Add(AngularResolutionData100A)

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

pionMC_Tree.Draw("chi2_Full>>hChi2_Full_pionMC1(200,0,10)")
data_Tree.Draw("chi2_Full>>hChi2_Full_data1(200,0,10)")
pionMC100A_Tree.Draw("chi2_Full>>hChi2_Full_pionMC100A1(200,0,10)")
data100A_Tree.Draw("chi2_Full>>hChi2_Full_data100A1(200,0,10)")

hChi2_Full_pionMC1.Add(hChi2_Full_pionMC100A1)
hChi2_Full_data1.Add(hChi2_Full_data100A1)

hChi2_Full_pionMC = hChi2_Full_pionMC1.Clone("d_Avg_MC")
hChi2_Full_pionMC.SetLineColor(kRed)
hChi2_Full_pionMC.SetLineWidth(2)
hChi2_Full_pionMC.Scale(1./hChi2_Full_pionMC.Integral())

hChi2_Full_data = hChi2_Full_data1.Clone("d_Avg_Data")
hChi2_Full_data.Scale(1./hChi2_Full_data.Integral())
hChi2_Full_data.SetMarkerStyle(21)
hChi2_Full_data.SetMarkerSize(0.5)
hChi2_Full_data.SetLineColor(kBlack)

hChi2_Full_pionMC.SetTitle("Average Spacepoint Distance from Fit; #bar{d} [cm]; Area Normalized Entries")
hChi2_Full_pionMC.Draw("histo")
hChi2_Full_data.Draw("pesames")
legend.Draw("same")

cTrackingDeg.Update()





raw_input()  











