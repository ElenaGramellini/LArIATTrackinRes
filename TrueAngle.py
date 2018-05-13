from ROOT import *
import os
import math
import argparse


# Get BeamComposition: percentage of pions, muons and electrons in a 60A beam configuration
#                       The beam at 60A is 
gStyle.SetOptStat(1101);

# Get Files' names
pionMC_FileName60A  = "/Volumes/Seagate/Elena/TPC/AngleCut_0.08334_histo_60A.root"
pionMC_FileName100A = "/Volumes/Seagate/Elena/TPC/AngleCut_100A_histo.root"

pionMC_File60A    = TFile.Open(pionMC_FileName60A)
pionMC_File100A   = TFile.Open(pionMC_FileName100A)

h_TrueAngleEl60A   = pionMC_File60A .Get("AngleCutTrueXS/h_AngleEl")
h_TrueAngleEl100A  = pionMC_File100A.Get("AngleCutTrueXS015/h_AngleEl")

cTrackingDeg = TCanvas("cAngleTrue" ,"cTracking" ,200 ,10 ,600 ,600)
cTrackingDeg.SetGrid()
h_TrueAngleEl60A.GetXaxis().SetLimits(-360.963,360.963)
h_TrueAngleEl60A.Rebin(2)
h_TrueAngleEl60A.GetXaxis().SetRangeUser(0.,180)
h_TrueAngleEl60A.GetYaxis().SetTitleOffset(1.8)
h_TrueAngleEl60A.Scale(1./h_TrueAngleEl60A.Integral())
h_TrueAngleEl60A.SetTitle("True Elastic Scattering Angle; Angle [Deg]; Normalized Entries")


h_TrueAngleEl100A.GetXaxis().SetLimits(-360.963,360.963)
h_TrueAngleEl100A.Rebin(2)
h_TrueAngleEl100A.GetXaxis().SetRangeUser(0.,180)
h_TrueAngleEl100A.GetYaxis().SetTitleOffset(1.8)
h_TrueAngleEl100A.Scale(1./h_TrueAngleEl100A.Integral())
h_TrueAngleEl100A.SetTitle("True Elastic Scattering Angle; Angle [Deg]; Normalized Entries")
h_TrueAngleEl100A.SetLineColor(kRed)



h_TrueAngleEl_All = h_TrueAngleEl60A.Clone("TrueElasticAngleEl")
h_TrueAngleEl_Draw60  = h_TrueAngleEl60A.Clone("TrueElasticAngleEl_60A")
h_TrueAngleEl_Draw100 = h_TrueAngleEl100A.Clone("TrueElasticAngleEl_100A")

h_TrueAngleEl_All.Add(h_TrueAngleEl100A)
h_TrueAngleEl_All.SetLineColor(kOrange)
h_TrueAngleEl_All.Scale(0.5)


h_TrueAngleEl_Draw100.Draw("histo")
h_TrueAngleEl_Draw60.Draw("histosames")
h_TrueAngleEl_All.Draw("histosames")


legend = TLegend(.54,.52,.84,.70);
legend.AddEntry(h_TrueAngleEl_Draw100,"MC 100A pions");
legend.AddEntry(h_TrueAngleEl_Draw60, "MC  60A pions");
legend.AddEntry(h_TrueAngleEl_All,"All  MC pions");
legend.Draw("same")


cTrackingDeg.Update()

raw_input()  



