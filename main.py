import os

def print_env_variables(variables):
    for var in variables:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value}")
        else:
            print(f"{var}: Not Set")

if __name__ == "__main__":
    env_vars = ["RAILWAY_DEPLOYMENT_ID", "RAILWAY_SNAPSHOT_ID", "RAILWAY_RUN_UID", "RAILWAY_ENVIRONMENT_NAME", "RAILWAY_PROJECT_NAME", "RAILWAY_GIT_COMMIT_SHA", "RAILWAY_GIT_REPO_NAME"]
    print_env_variables(env_vars)
