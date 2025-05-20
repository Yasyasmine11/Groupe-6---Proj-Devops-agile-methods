# Affichage console simple
def print_build_dashboard(builds):
    print("Derniers Builds:")
    for build in builds['value'][:5]:
        print(f"{build['buildNumber']} - {build['status']} - {build['result']}")
