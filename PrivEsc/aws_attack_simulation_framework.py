import json
import subprocess

def execute_attack_scenario(attack_scenario):
    attack_name = attack_scenario['name']
    print(f"Executing attack scenario: {attack_name}")

    # Execute attack module
    subprocess.run(['python', 'privilege_escalation_attack.py'])

def main():
    # Load attack scenario configuration
    with open('privilege_escalation_scenario.json', 'r') as config_file:
        attack_scenario = json.load(config_file)

    # Execute attack scenario
    execute_attack_scenario(attack_scenario)

if __name__ == "__main__":
    main()
