import qiskit
import matplotlib.pyplot as plt

# Create Quantum Circut with 1 Qubit
circuit = qiskit.QuantumCircuit(1, 1)

# Molecular initial state simulation
circuit.h(0) # We apply the Hadamard operator to create a superposition

# Simulation of a "barrier" - we simulate uncertainty about the passage
circuit.x(0)  # Pauli-X operator acts as a "barrier"

#Particle state measurement
circuit.measure(0, 0)

# Circut drawing
circuit.draw('mpl')
plt.show()

# Simulation on local Aer simulator
simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(circuit, simulator, shots=1000).result()
counts = result.get_counts()

# Results visualization
plt.bar(counts.keys(), counts.values())
plt.xlabel('Stan końcowy')
plt.ylabel('Liczba pomiarów')
plt.title('Symulacja tunelowania kwantowego')
plt.show()
