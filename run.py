from Sim import simulate_game

def run(deck, n=10000):

    setup_count = 0
    optimalSetup_count = 0
    recovery_count = 0
    pressure_count = 0
    first_games = 0
    second_games = 0

    # New counters for individual registrations
    setup_if_first_count = 0
    optimal_setup_if_first_count = 0
    recovery_if_first_count = 0
    pressure_if_first_count = 0
    setup_if_second_count = 0
    optimal_setup_if_second_count = 0
    recovery_if_second_count = 0
    pressure_if_second_count = 0

    for _ in range(n):

        result = simulate_game(deck)

        # Unpack the dictionary
        setup = result["setup"]
        optimal_setup = result["optimal_setup"]
        recovery = result["recovery"]
        pressure = result["pressure"]
        going_first = result["going_first"]

        setup_count += setup
        optimalSetup_count += optimal_setup
        recovery_count += (setup and recovery)
        pressure_count += pressure

        if going_first:
            first_games += 1
        else:
            second_games += 1

        # Add counts for individual cases
        setup_if_first_count += result["setup_if_first"]
        optimal_setup_if_first_count += result["optimal_setup_if_first"]
        recovery_if_first_count += (result["setup_if_first"] and result["recovery_if_first"])
        pressure_if_first_count += result["pressure_if_first"]

        setup_if_second_count += result["setup_if_second"]
        optimal_setup_if_second_count += result["optimal_setup_if_second"]
        recovery_if_second_count += (result["setup_if_second"] and result["recovery_if_second"])
        pressure_if_second_count += result["pressure_if_second"]

    return {
        "setup_rate": setup_count / n,
        "optimalsetup_rate": optimalSetup_count / n,
        "recovery_rate": recovery_count / n,
        "pressure_rate": pressure_count / n,
        # New: Rates for if going first
        "setup_if_first_rate": setup_if_first_count / n,
        "optimal_setup_if_first_rate": optimal_setup_if_first_count / n,
        "recovery_if_first_rate": recovery_if_first_count / n,
        "pressure_if_first_rate": pressure_if_first_count / n,
        # New: Rates for if going second
        "setup_if_second_rate": setup_if_second_count / n,
        "optimal_setup_if_second_rate": optimal_setup_if_second_count / n,
        "recovery_if_second_rate": recovery_if_second_count / n,
        "pressure_if_second_rate": pressure_if_second_count / n,
    }

def print_analysis(deck_name, results):
    print(f"=== {deck_name} ===")
    print(f"Setup Rate: {results['setup_rate']:.2f}")
    print(f"Optimal Setup Rate: {results['optimalsetup_rate']:.2f}")
    print(f"Recovery Rate: {results['recovery_rate']:.2f}")
    print(f"Pressure Rate: {results['pressure_rate']:.2f}")
    print()
    print("If going first:")
    print(f"Setup Rate: {results['setup_if_first_rate']:.2f}")
    print(f"Optimal Setup Rate: {results['optimal_setup_if_first_rate']:.2f}")
    print(f"Recovery Rate: {results['recovery_if_first_rate']:.2f}")
    print(f"Pressure Rate: {results['pressure_if_first_rate']:.2f}")
    print()
    print("If going second:")
    print(f"Setup Rate: {results['setup_if_second_rate']:.2f}")
    print(f"Optimal Setup Rate: {results['optimal_setup_if_second_rate']:.2f}")
    print(f"Recovery Rate: {results['recovery_if_second_rate']:.2f}")
    print(f"Pressure Rate: {results['pressure_if_second_rate']:.2f}")
    print()
    print("Analysis:")
    setup_diff = results["setup_if_first_rate"] - results["setup_if_second_rate"]
    optimal_diff = results["optimal_setup_if_first_rate"] - results["optimal_setup_if_second_rate"]
    recovery_diff = results["recovery_if_first_rate"] - results["recovery_if_second_rate"]
    pressure_diff = results["pressure_if_first_rate"] - results["pressure_if_second_rate"]
    print(f"Setup Rate Difference (First - Second): {setup_diff:.2f}")
    print(f"Optimal Setup Rate Difference: {optimal_diff:.2f}")
    print(f"Recovery Rate Difference: {recovery_diff:.2f}")
    print(f"Pressure Rate Difference: {pressure_diff:.2f}")
    print()