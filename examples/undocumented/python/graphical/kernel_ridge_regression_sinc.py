import matplotlib.pyplot as plt
import shogun as sg
import util

plt.figure('KernelRidgeRegression on Sine')

X, Y = util.get_sinedata()

feat = sg.create_features(X)
lab = sg.create_labels(Y.flatten())
gk = sg.create('GaussianKernel', width=1.0)
gk.init(feat, feat)
krr = sg.create('KernelRidgeRegression', labels=lab, kernel=gk, tau=1e-3)
krr.train()

plt.scatter(X, Y,  label='train data', color='tab:red')
plt.plot(X[0], krr.apply().get('labels'), label='train output')

XE, YE = util.compute_output_plot_isolines_sine(krr, gk, feat, regression=True)
YE200 = krr.apply_one(200)

plt.plot(XE[0], YE, label='test output')
plt.plot([XE[0, 200]], [YE200], '+')

plt.legend()
plt.show()
