import argparse
from solution_1.main import transform_data as solution_1_transfotrm
from solution_2.main import transform_data as solution_2_transfotrm


parser = argparse.ArgumentParser(
    description="A script that accepts data source name"
)

parser.add_argument(
    "--solution",
    default="solution_2",
    required=False,
    help="Pleas enter solution_1 or solution_2"
)

parser.add_argument(
    "--datasource-name",
    default="datasource_a",
    required=False,
    help="The name of the data source"
)

args = parser.parse_args()

def main():
    solution = args.solution
    datasource_name = args.datasource_name

    if solution == "solution_1":
        # This is the solution without using dynamic import
        print(f"[{solution}] Start to transform data without using dynamic import for data source {datasource_name}")
        solution_1_transfotrm(datasource_name)
        

    elif solution == "solution_2":
        # This is the solution with using dynamic import
        print(f"[{solution}] Start to transform data with using dynamic import for data source {datasource_name}")
        solution_2_transfotrm(datasource_name)
        
    else:
        print("You entered an invalid solution. Please enter solution_1 or solution_2")

if __name__ == "__main__":
    main()