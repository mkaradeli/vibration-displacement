#	m_car ve m_wheel	birimi Kg
#	speed 				birimi kph
#	wheelDiameter 		birimi metre
#	eccentricity 		birimi metre
#	k ve zeta 			sabit
import math

def natFreqInHz(k, m_wheel): # in Hz
	return math.sqrt(k/m) / (2 * math.pi)

def natFreqInRadSec(k, m_wheel)	#in Rad/sec
	return (natFreqInHz(k, m_wheel) * 2 * math.pi)

def operatingFreqInRadSec(speed, wheelDiameter) # speed in kph	-	wheelDiameter in m
	return (speed/3.6/wheelDiameter*2p)

def freqRatio(k, m_wheel, speed, wheelDiameter) # a.k.a. => 	r
	return(natFreqInRadSec(k, m_wheel)/operatingFreqInRadSec(speed, wheelDiameter))

def steadyStateAmplitude(m_wheel, m_car, speed, wheelDiameter, eccentricity, k, zeta)
	r = freqRatio(k, m_wheel, speed, wheelDiameter)
	return((m_wheel*eccentricity/m_car)*((r^2) / math.sqrt((1-r^2)^2 + (2*r*zeta)^2)))


