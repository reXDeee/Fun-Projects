# Function to calculate Fire Power Score (FPS)
def calculate_fps(lethality, rate_of_fire, range_eff, ammo_capacity, accuracy):
    # Normalize inputs to have values between 0 and 1
    lethality_norm = lethality / 100
    rate_of_fire_norm = rate_of_fire / 100
    range_norm = range_eff / 100
    ammo_capacity_norm = ammo_capacity / 100
    accuracy_norm = accuracy / 100

    # FPS as a weighted sum of the factors
    fps = 0.3 * lethality_norm + 0.2 * rate_of_fire_norm + 0.2 * range_norm + 0.15 * ammo_capacity_norm + 0.15 * accuracy_norm
    return fps * 100  # Convert to percentage

# Function to calculate Weapon Power Score (WPS)
def calculate_wps(fps, survivability, operability, integration):
    # Normalize additional factors
    survivability_norm = survivability / 100
    operability_norm = operability / 100
    integration_norm = integration / 100

    # WPS as a weighted sum
    wps = 0.5 * (fps / 100) + 0.2 * survivability_norm + 0.15 * operability_norm + 0.15 * integration_norm
    return wps * 100  # Convert to percentage

# Function to calculate Generalized Weapon Power Score (GWPS)
def calculate_gwps(wps, terrain_factor, mobility_factor, conflict_intensity):
    # Normalize the environmental factors
    terrain_factor_norm = terrain_factor / 100
    mobility_factor_norm = mobility_factor / 100
    conflict_intensity_norm = conflict_intensity / 100

    # GWPS is WPS adjusted for operational environment
    gwps = (wps / 100) * (1 + terrain_factor_norm) * (1 + mobility_factor_norm) * (1 + conflict_intensity_norm)
    return gwps * 100  # Convert to percentage

# Function to get user input for weapon scores and environment factors
def get_weapon_data():
    name = input("Enter the name of the weapon: ")
    
    lethality = float(input("Enter lethality score (0-100): "))
    rate_of_fire = float(input("Enter rate of fire score (0-100): "))
    range_eff = float(input("Enter range effectiveness score (0-100): "))
    ammo_capacity = float(input("Enter ammunition capacity score (0-100): "))
    accuracy = float(input("Enter accuracy score (0-100): "))
    survivability = float(input("Enter survivability score (0-100): "))
    operability = float(input("Enter operability score (0-100): "))
    integration = float(input("Enter integration score (0-100): "))
    
    terrain_factor = float(input("Enter terrain factor (0-100): "))
    mobility_factor = float(input("Enter mobility factor (0-100): "))
    conflict_intensity = float(input("Enter conflict intensity (0-100): "))
    
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

# Function to calculate scores based on user inputs
def calculate_scores(weapon_data):
    fps = calculate_fps(weapon_data['lethality'], weapon_data['rate_of_fire'], weapon_data['range_eff'], 
                        weapon_data['ammo_capacity'], weapon_data['accuracy'])
    
    wps = calculate_wps(fps, weapon_data['survivability'], weapon_data['operability'], weapon_data['integration'])
    
    gwps = calculate_gwps(wps, weapon_data['terrain_factor'], weapon_data['mobility_factor'], weapon_data['conflict_intensity'])
    
    return {
        'name': weapon_data['name'],
        'FPS': fps,
        'WPS': wps,
        'GWPS': gwps
    }

# Example of running the program
weapon_data = get_weapon_data()
scores = calculate_scores(weapon_data)
print(f"Weapon: {scores['name']}, FPS: {scores['FPS']:.2f}, WPS: {scores['WPS']:.2f}, GWPS: {scores['GWPS']:.2f}")
