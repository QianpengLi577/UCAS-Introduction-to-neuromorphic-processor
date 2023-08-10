import matplotlib.pyplot as plt
import numpy as np


def default_pars(**kwargs):
	pars = {}

	# typical neuron parameters#
	pars['V_th'] = -55.     # spike threshold [mV]
	pars['V_reset'] = -75.  # reset potential [mV]
	pars['tau_m'] = 10.     # membrane time constant [ms]
	pars['R'] = 0.1         # resistance [MΩ]  
	pars['V_init'] = -75.   # initial potential [mV]
	pars['V_rest'] = -75.   # rest potential [mV]

	# simulation parameters #
	pars['T'] = 400.  # Total duration of simulation [ms]
	pars['dt'] = .1   # Simulation time step [ms]

	# external parameters if any #
	for k in kwargs:
		pars[k] = kwargs[k]

	pars['range_t'] = np.arange(0, pars['T'], pars['dt'])  # Vector of discretized time points [ms]

	return pars

def plot_volt_trace(pars, v, sp, save_pic=False, pic_name=''):
	"""
	Plot trajetory of membrane potential for a single neuron

	Expects:
	pars     : parameter dictionary
	v        : volt trajetory
	sp       : spike train
	save_pic : save pic
	pic_name : if save_pic is True, save the pic with pic_name.png

	Returns:
	figure of the membrane potential trajetory for a single neuron
	"""

	V_th = pars['V_th']
	dt, range_t = pars['dt'], pars['range_t']
	if sp.size:
		sp_num = (sp / dt).astype(int) - 1
		v[sp_num] += 20  # draw nicer spikes

	plt.plot(pars['range_t'], v, 'b')
	plt.axhline(V_th, 0, 1, color='k', ls='--')
	plt.xlabel('Time (ms)')
	plt.ylabel('V (mV)')
	plt.legend(['Membrane\npotential', r'Threshold V$_{\mathrm{th}}$'],
			 loc=[0.80, 0.75])
	plt.ylim([-80, -40])
	ax=plt.gca()  
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	if save_pic is True:
		plt.savefig(pic_name+'.png')
	plt.show()

def plot_volt_trace_gif(pars, v, sp, save_pic=False, pic_name=''):
	"""
	Plot trajetory of membrane potential for a single neuron

	Expects:
	pars     : parameter dictionary
	v        : volt trajetory
	sp       : spike train
	save_pic : save pic
	pic_name : if save_pic is True, save the pic with pic_name.png

	Returns:
	figure of the membrane potential trajetory for a single neuron
	"""
	plt.ion()
	plt.figure()

	V_th = pars['V_th']
	dt, range_t = pars['dt'], pars['range_t']
	if sp.size:
		sp_num = (sp / dt).astype(int) - 1
		v[sp_num] += 20  # draw nicer spikes

	time_steps = len(v)
	for t in range(time_steps):
		plt.plot(range_t[:t], v[:t], 'b')
		plt.axhline(V_th, 0, 1, color='k', ls='--')
		plt.xlabel('Time (ms)')
		plt.ylabel('V (mV)')
		plt.legend(['Membrane\npotential', r'Threshold V$_{\mathrm{th}}$'],
					loc=[0.80, 0.75])
		plt.ylim([-80, -40])
		ax=plt.gca()  
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		if save_pic is True:
			plt.savefig('./pic/' + pic_name + str(t) + '.png')
	plt.ioff()
	plt.show()
