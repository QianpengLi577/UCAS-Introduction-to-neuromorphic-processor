from neuron_tools import *

def run_LIF(pars, Iinj, stop=False):
	"""
	Simulate the LIF dynamics with external input current

	Args:
		pars       : parameter dictionary
		Iinj       : input current [pA]. The injected current here can be a value
								 or an array
		stop       : boolean. If True, use a current pulse

	Returns:
		rec_v      : membrane potential
		rec_sp     : spike times
	"""

	# Set parameters
	V_th, V_reset = pars['V_th'], pars['V_reset']
	tau_m, R = pars['tau_m'], pars['R']
	V_init, E_L = pars['V_init'], pars['V_rest']
	dt, range_t = pars['dt'], pars['range_t']
	Lt = range_t.size

	# Initialize voltage
	v = np.zeros(Lt)
	v[0] = V_init

	# A simple example of input spike train

	Iinj = Iinj * np.ones(Lt)
	# set beginning and end to 0
	if stop:
		Iinj[:int(len(Iinj) / 2) - 600] = 0
		Iinj[int(len(Iinj) / 2) + 600:] = 0

	# Loop over time
	rec_spikes = []  # record spike times
	tr = 0.  # the count for refractory duration

	for it in range(Lt - 1):

		if v[it] >= V_th:  # if voltage over threshold
			rec_spikes.append(it)  # record spike event
			v[it] = V_reset  # reset voltage

		# Update the membrane potential
		v[it + 1] = ( 1 - (dt / tau_m) )*v[it] + (E_L + Iinj[it] * R) * (dt / tau_m)

	# Get spike times in ms
	rec_spikes = np.array(rec_spikes) * dt

	return v, rec_spikes

if __name__ == '__main__':
	# Get parameters
	pars = default_pars(T=400)

	# Simulate LIF model
	v, sp = run_LIF(pars, Iinj=100, stop=True)

	# Visualize

	plot_volt_trace(pars, v, sp, True, 'lif')
	# plot_volt_trace_gif(pars, v, sp, False, 'lif')