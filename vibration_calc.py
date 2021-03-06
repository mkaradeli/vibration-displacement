#	m_car ve m_wheel	birimi Kg
#	speed				birimi kph
#	wheelDiameter 		birimi metre
#	eccentricity 		birimi metre
#	k ve zeta			sabit
#	steadyStateAmplitude sonuç birimi metre
#
#	example
#	>>> steadyStateAmplitude(5, 500, 120, 0.4, 0.02, 100, 0.001)
#	0.00020014410346608043

import math

def natFreqInHz(k, m_wheel): # in Hz
	return math.sqrt(k/m_wheel) / (2 * math.pi)

def natFreqInRadSec(k, m_wheel):	#in Rad/sec
	return (natFreqInHz(k, m_wheel) * 2 * math.pi)

def operatingFreqInRadSec(speed, wheelDiameter): # speed in kph	-	wheelDiameter in m
	return (2 * math.pi * speed/(3.6*wheelDiameter* math.pi))

def freqRatio(k, m_wheel, speed, wheelDiameter): # a.k.a. => 	r
	return(operatingFreqInRadSec(speed, wheelDiameter)/natFreqInRadSec(k, m_wheel))

def steadyStateAmplitude(m_wheel, m_car, speed, wheelDiameter, eccentricity, k, zeta):
	r = freqRatio(k, m_wheel, speed, wheelDiameter)
	return((m_wheel*eccentricity/m_car)*((r*r) / math.sqrt(math.pow(1-r*r, 2) + math.pow(2*r*zeta, 2))))
