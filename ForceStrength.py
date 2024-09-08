# Importing numpy is no longer necessary for this code
# ---------------------- Weapon System Evaluation (Chapter 10) ----------------------

# Function to calculate Fire Power Score (FPS)
def calculate_fps(lethality, rate_of_fire, range_eff, ammo_capacity, accuracy):
    lethality_norm = lethality / 100
    rate_of_fire_norm = rate_of_fire / 100
    range_norm = range_eff / 100
    ammo_capacity_norm = ammo_capacity / 100
    accuracy_norm = accuracy / 100

    fps = 0.3 * lethality_norm + 0.2 * rate_of_fire_norm + 0.2 * range_norm + 0.15 * ammo_capacity_norm + 0.15 * accuracy_norm
    return fps * 100  # Convert to percentage

# Function to calculate Weapon Power Score (WPS)
def calculate_wps(fps, survivability, operability, integration):
    survivability_norm = survivability / 100
    operability_norm = operability / 100
    integration_norm = integration / 100

    wps = 0.5 * (fps / 100) + 0.2 * survivability_norm + 0.15 * operability_norm + 0.15 * integration_norm
    return wps * 100  # Convert to percentage

# Function to calculate Generalized Weapon Power Score (GWPS)
def calculate_gwps(wps, terrain_factor, mobility_factor, conflict_intensity):
    terrain_factor_norm = terrain_factor / 100
    mobility_factor_norm = mobility_factor / 100
    conflict_intensity_norm = conflict_intensity / 100

    gwps = (wps / 100) * (1 + terrain_factor_norm) * (1 + mobility_factor_norm) * (1 + conflict_intensity_norm)
    return gwps * 100  # Convert to percentage

# ---------------------- RMA Index and Force Potential (Chapter 11) ----------------------

# Function to calculate RMA Index
def calculate_rma_index(isr_weight, c4_weight, iw_weight, ilss_weight, isr_capability, c4_capability, iw_capability, ilss_capability):
    rma_index = (isr_weight * isr_capability +
                 c4_weight * c4_capability +
                 iw_weight * iw_capability +
                 ilss_weight * ilss_capability)
    return rma_index

# Function to calculate Force Strength (FS) and Force Potential (FP)
def calculate_force_potential(weapon_systems_gwps, rma_index):
    force_strength = sum(weapon_systems_gwps)
    force_potential = force_strength * rma_index
    return force_strength, force_potential

# ---------------------- Dynamic Input for Weapons and RMA ----------------------

# Function to get input for weapon data
def get_weapon_data():
    name = input("Enter the name of the weapon: ")
    
    lethality = float(input(f"Enter lethality score for {name} (0-100): "))
    rate_of_fire = float(input(f"Enter rate of fire score for {name} (0-100): "))
    range_eff = float(input(f"Enter range effectiveness score for {name} (0-100): "))
    ammo_capacity = float(input(f"Enter ammunition capacity score for {name} (0-100): "))
    accuracy = float(input(f"Enter accuracy score for {name} (0-100): "))
    survivability = float(input(f"Enter survivability score for {name} (0-100): "))
    operability = float(input(f"Enter operability score for {name} (0-100): "))
    integration = float(input(f"Enter integration score for {name} (0-100): "))
    
    terrain_factor = float(input(f"Enter terrain factor for {name} (0-100): "))
    mobility_factor = float(input(f"Enter mobility factor for {name} (0-100): "))
    conflict_intensity = float(input(f"Enter conflict intensity for {name} (0-100): "))
    
    return {
        'name': name,
        'lethality': lethality,
        'rate_of_fire': rate_of_fire,
        'range_eff': range_eff,
        'ammo_capacity': ammo_capacity,
        'accuracy': accuracy,
        'survivability': survivability,
        'operability': operability,
        'integration': integration,
        'terrain_factor': terrain_factor,
        'mobility_factor': mobility_factor,
        'conflict_intensity': conflict_intensity
    }

# Function to get input for RMA components
def get_rma_data():
    print("Enter RMA component weights and capabilities (0-1 for weights, 0-100 for capabilities)")
    
    isr_weight = float(input("Enter ISR weight (0-1): "))
    c4_weight = float(input("Enter C4 weight (0-1): "))
    iw_weight = float(input("Enter IW weight (0-1): "))
    ilss_weight = float(input("Enter ILSS weight (0-1): "))

    isr_capability = float(input("Enter ISR capability (0-100): "))
    c4_capability = float(input("Enter C4 capability (0-100): "))
    iw_capability = float(input("Enter IW capability (0-100): "))
    ilss_capability = float(input("Enter ILSS capability (0-100): "))

    return {
        'weights': {
            'ISR': isr_weight,
            'C4': c4_weight,
            'IW': iw_weight,
            'ILSS': ilss_weight
        },
        'capabilities': {
            'ISR': isr_capability,
            'C4': c4_capability,
            'IW': iw_capability,
            'ILSS': ilss_capability
        }
    }

# ---------------------- Main Program ----------------------

def main():
    # Collect multiple weapon systems data
    weapon_systems = []
    num_weapons = int(input("Enter the number of weapon systems: "))

    for i in range(num_weapons):
        print(f"\nCollecting data for weapon {i+1}:")
        weapon_data = get_weapon_data()
        weapon_systems.append(weapon_data)

    # Calculate GWPS for each weapon system
    weapon_systems_gwps = []
    for weapon in weapon_systems:
        fps = calculate_fps(weapon['lethality'], weapon['rate_of_fire'], weapon['range_eff'], 
                            weapon['ammo_capacity'], weapon['accuracy'])
    
        wps = calculate_wps(fps, weapon['survivability'], weapon['operability'], weapon['integration'])
    
        gwps = calculate_gwps(wps, weapon['terrain_factor'], weapon['mobility_factor'], weapon['conflict_intensity'])
        
        weapon_systems_gwps.append(gwps)
        print(f"Weapon: {weapon['name']}, FPS: {fps:.2f}, WPS: {wps:.2f}, GWPS: {gwps:.2f}")

    # Get RMA data
    rma_data = get_rma_data()

    # Calculate the RMA Index
    rma_index = calculate_rma_index(
        rma_data['weights']['ISR'], rma_data['weights']['C4'], rma_data['weights']['IW'], rma_data['weights']['ILSS'],
        rma_data['capabilities']['ISR'], rma_data['capabilities']['C4'], rma_data['capabilities']['IW'], rma_data['capabilities']['ILSS']
    )

    # Calculate Force Strength and Force Potential
    force_strength, force_potential = calculate_force_potential(weapon_systems_gwps, rma_index)

    # Output the results
    print(f"\nTotal Force Strength: {force_strength:.2f}")
    print(f"RMA Index: {rma_index:.2f}")
    print(f"Total Force Potential: {force_potential:.2f}")

if __name__ == "__main__":
    main()
1