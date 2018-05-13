from ROOT import *
import os
import math
import argparse

gStyle.SetOptStat(0);

noAngleCutFile   = TFile.Open("/Volumes/Seagate/Elena/TPC/AngleCut_100A_histo.root")
angleCutFile0157 = TFile.Open("TruePionGen60A.root")
#angleCutFile0092 = TFile.Open("AngleCut_0.09248_histo.root")
#angleCutFile0083 = TFile.Open("AngleCut_0.08334_histo.root")
#angleCutFile0079 = TFile.Open("AngleCut_0.07954_histo.root")

# Get Interacting and Incident plots
interactingName = "AngleCutTrueXS/hInteractingKE"
incidentName = "AngleCutTrueXS/hIncidentKE"

noAngleCut_Int    = noAngleCutFile   .Get("TrueXS/hInteractingKE")
angleCut_Int_0157 = angleCutFile0157 .Get("TrueXS/hInteractingKE")
#angleCut_Int_0092 = angleCutFile0092 .Get(interactingName)
#angleCut_Int_0083 = angleCutFile0083 .Get(interactingName)
#angleCut_Int_0079 = angleCutFile0079 .Get(interactingName)

noAngleCut_Inc    = noAngleCutFile   .Get("TrueXS/hIncidentKE")
angleCut_Inc_0157 = angleCutFile0157 .Get("TrueXS/hIncidentKE")
#angleCut_Inc_0092 = angleCutFile0092 .Get(incidentName)
#angleCut_Inc_0083 = angleCutFile0083 .Get(incidentName)
#angleCut_Inc_0079 = angleCutFile0079 .Get(incidentName)

noAngleCutXS    = noAngleCut_Int    .Clone("noAngleCutXS")
angleCutXS_0157 = angleCut_Int_0157 .Clone("angleCutXS_0157")
#angleCutXS_0092 = angleCut_Int_0092 .Clone("angleCutXS_0092")
#angleCutXS_0083 = angleCut_Int_0083 .Clone("angleCutXS_0083")
#angleCutXS_0079 = angleCut_Int_0079 .Clone("angleCutXS_0079")

noAngleCutXS   .Scale(101.)
angleCutXS_0157.Scale(101.)
#angleCutXS_0092.Scale(101.)
#angleCutXS_0083.Scale(101.)
#angleCutXS_0079.Scale(101.)

#for i in xrange(6):
#    noAngleCut_Inc.SetBinContent(i,0)
#    angleCutXS_0157.SetBinContent(i,0)
#    angleCutXS_0092.SetBinContent(i,0)
#    angleCutXS_0083.SetBinContent(i,0)
#    angleCutXS_0079.SetBinContent(i,0)

#for i in xrange(21,40):
#    noAngleCut_Inc.SetBinContent(i,0)
#    angleCutXS_0157.SetBinContent(i,0)
#    angleCutXS_0092.SetBinContent(i,0)
#    angleCutXS_0083.SetBinContent(i,0)
#    angleCutXS_0079.SetBinContent(i,0)

noAngleCutXS   .Divide(noAngleCut_Inc   )
angleCutXS_0157.Divide(angleCut_Inc_0157)
#angleCutXS_0092.Divide(angleCut_Inc_0092)
#angleCutXS_0083.Divide(angleCut_Inc_0083)
#angleCutXS_0079.Divide(angleCut_Inc_0079)


angleCutXS_0157.SetLineColor(kRed)


#noAngleCutXS.SetLineColor(kGreen-2)
#angleCutXS_0083.SetLineColor(kRed)
#angleCutXS_0157.SetLineColor(kBlue)
#angleCutXS_0083.SetLineWidth(2)

cTracking = TCanvas("cTracking" ,"cTracking" ,200 ,10 ,600 ,600)
cTracking.SetGrid()
noAngleCutXS.SetTitle("(#pi^{-},Ar) True Cross Section above a given angle selection; Kinetic Energy [MeV];  (#pi^{-},Ar) True Cross Section [barn]")
noAngleCutXS   .Draw("histope][") 
angleCutXS_0157 .Draw("histosamepe][") 
#angleCutXS_0092 .Draw("histosame][") 
#angleCutXS_0083 .Draw("histosame][") 
#angleCutXS_0079 .Draw("histosame][") 


legend = TLegend(.54,.52,.84,.70)
legend.AddEntry(noAngleCutXS  ,"All Angles 100 A")
legend.AddEntry(angleCutXS_0157  ,"All Angles 600 A")
#legend.AddEntry(angleCutXS_0079,"Angles > 4.5 Deg")
#legend.AddEntry(angleCutXS_0083,"Angles > 5.0 Deg")
#legend.AddEntry(angleCutXS_0092,"Angles > 4.5 Deg")
#legend.AddEntry(angleCutXS_0157,"Angles > 9.5 Deg")


legend.Draw("same")
cTracking.Update()




raw_input()  



