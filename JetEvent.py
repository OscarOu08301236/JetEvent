import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# declare global constant 
threshold_energy = 0.1
deterministic_time = 1

# store coordinate for plotting
coordinate = []

# Generate random z for energy decay
def randomZ():
    z = np.random.random() * np.log(2)
    return np.e**z - 1

# Generate random theta for decay degree
def randomTheta():
    theta = np.random.random() * np.log(np.pi / 2 + 1)
    return np.e**theta - 1

# Generate random phi for 3D degree
def randomPhi():
    phi = np.random.random() * np.pi
    return phi

# Paricle class with E, px, py, pz information
class Particle():
    def __init__(self, E, px, py, pz, theta_angle, phi_angle, gen):
        self.E = E
        self.px = px
        self.py = py
        self.pz = pz 
        self.theta_angle = theta_angle
        self.phi_angle = phi_angle
        self.gen = gen

    # def __str__(self):

    def getP(self):
        return (self.px**2 + self.py**2 + self.pz**2)**0.5

    def getVelocity(self):
        p = self.getP()
        v = 2 * self.E / p
        vx = v * np.cos(self.phi_angle) * np.sin(self.theta_angle)
        vy = v * np.sin(self.phi_angle) * np.sin(self.theta_angle)
        vz = v * np.cos(self.theta_angle)
        return (v, vx, vy, vz)

# function that perform the jet event 
def jetEvent(prev_particle, x = 0, y = 0, z = 0):

    # if the particle don't have enough energy to decay
    if(prev_particle.E <= threshold_energy):
        return [prev_particle]

    else:
        # deterministic time travel
        prev_velocity = prev_particle.getVelocity()
        new_x = prev_velocity[1] * deterministic_time + x
        new_y = prev_velocity[2] * deterministic_time + y
        new_z = prev_velocity[3] * deterministic_time + z
        coordinate.append((x, y, z, new_x, new_y, new_z))

        # generate random constant
        new_theta = randomTheta()
        new_phi = randomPhi()
        new_z_constant = randomZ() 

        # deal with new particle 1
        new_energy_1 = prev_particle.E * new_z_constant
        new_p_1 = prev_particle.getP() * np.sqrt(new_z_constant)
        new_px_1 = new_p_1 * np.cos(prev_particle.phi_angle + new_phi)
        new_py_1 = new_p_1 * np.sin(prev_particle.phi_angle + new_phi)
        new_pz_1 = new_p_1 * np.cos(prev_particle.theta_angle + new_theta)

        new_particle_1 = Particle(new_energy_1, new_px_1, new_py_1, new_pz_1, 
                        prev_particle.phi_angle + new_phi, prev_particle.theta_angle + new_theta, prev_particle.gen + 1)
            
        # deal with new particle 2 
        new_energy_2 = prev_particle.E - new_energy_1
        new_p_2 = prev_particle.getP() - new_p_1 # not necessary
        new_px_2 = prev_particle.px - new_px_1
        new_py_2 = prev_particle.py - new_py_1
        new_pz_2 = prev_particle.pz - new_pz_1

        new_particle_2 = Particle(new_energy_2, new_px_2, new_py_2, new_pz_2, 
                        prev_particle.phi_angle - new_phi, prev_particle.theta_angle - new_theta, prev_particle.gen + 1)

        # recursion 
        return jetEvent(new_particle_1, new_x, new_y, new_z) + jetEvent(new_particle_2, new_x, new_y, new_z)


# Test method for the random generation of 
def showGraph():
    result_z = []
    result_theta = []
    result_phi = []
    i = 0
    for i in range(0, 1000):
        result_z.append(randomZ())
        result_theta.append(randomTheta())
        result_phi.append(randomPhi())
        i += 1

    plt.title("Random Numbers")
    plt.xlabel("Values")
    plt.ylabel("Counts")
    plt.hist(result_z)
    plt.show()
    plt.hist(result_theta)
    plt.show()
    plt.hist(result_phi)
    plt.show()

showGraph()
