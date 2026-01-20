import numpy as np 
import matplotlib.pyplot as plt 
import uproot 
from scipy.integrate import simpson

file = uproot.open('/home/public/data/ggH125/ZZ4lAnalysis.root')
tree = file["ZZTree/candTree"]

sigma = np.array(tree["xsec"].array())
w_event = np.array(tree["overallEventWeight"].array())

counters = file["ZZTree/Counters"]
counts, edges = counters.to_numpy()
sum_w = counts[39]

L = 137000
weights_signal = L * sigma * w_event / sum_w

file_bkg = uproot.open("/home/public/data/qqZZ/ZZ4lAnalysis.root")
tree_bkg = file_bkg["ZZTree/candTree"]

sigma_bkg = np.array(tree_bkg["xsec"].array())
w_event_bkg = np.array(tree_bkg["overallEventWeight"].array())

counts_bkg, _ = file_bkg["ZZTree/Counters"].to_numpy()
sum_w_bkg = counts_bkg[39]

weights_background = L * sigma_bkg * w_event_bkg / sum_w_bkg



p_signal = np.array(tree["p_GG_SIG_ghg2_1_ghz1_1_JHUGen"].array())
p_background = np.array(tree["p_QQB_BKG_MCFM"].array())

p_signal_bkg = np.array(tree_bkg["p_GG_SIG_ghg2_1_ghz1_1_JHUGen"].array())
p_background_bkg = np.array(tree_bkg["p_QQB_BKG_MCFM"].array())

d_signal = 1.0 / (1.0 + 1 * (p_background / p_signal))
d_background = 1.0 / (1.0 + 70 * (p_background_bkg / p_signal_bkg))


plt.figure(figsize=(7,5))
plt.hist(d_signal, bins=100, weights=weights_signal,
         density=True, alpha=0.6, label="Signal")

plt.hist(d_background, bins=100, weights=weights_background,
         density=True, alpha=0.6, label="Background")

plt.xlabel(r"$D^{bkg}_{kin}$")
plt.ylabel("Normalized events")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("background-signal-hist.jpg")
plt.close()


thresholds = np.linspace(0, 1, 1001)

sig_eff = []
bkg_eff = []

for t in thresholds:
    sig_eff.append(np.sum(weights_signal[d_signal > t]) / np.sum(weights_signal))
    bkg_eff.append(np.sum(weights_background[d_background > t]) / np.sum(weights_background))

plt.plot(bkg_eff, sig_eff)
plt.xlabel("Background efficiency")
plt.ylabel("Signal efficiency")
plt.savefig('roc.jpg')
plt.close()


hist_sig, bins = np.histogram(
    d_signal, bins=100, range=(0,1),
    weights=weights_signal, density=False
)

hist_bkg, _ = np.histogram(
    d_background, bins=bins,
    weights=weights_background, density=False
)

Nsig = np.sum(hist_sig)
Nbkg = np.sum(hist_bkg)

sig_eff = np.cumsum(hist_sig[::-1])[::-1] / Nsig
bkg_eff = np.cumsum(hist_bkg[::-1])[::-1] / Nbkg

plt.figure(figsize=(6,6))
plt.plot(bkg_eff, sig_eff, drawstyle="steps-post")
plt.xlabel("Background efficiency")
plt.savefig("roc-hist.jpg")
plt.close()

auc_hist = simpson(sig_eff, bkg_eff)
print("AUC (histogram):", auc_hist)