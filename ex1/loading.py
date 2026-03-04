import sys


def support(item: dict) -> int:
    return item.get('year')


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    fail = False
    try:
        import pandas
        # prints the name and version of the package
        print(f"[OK] {pandas.__name__} ({pandas.__version__}) "
              "- Data manipulation ready")
    except ImportError:
        print("[KO] pandas not found")
        fail = True
    try:
        import requests
        # prints the name and version of the package
        print(f"[OK] {requests.__name__} ({requests.__version__}) "
              "- Network access ready")
    except ImportError:
        print("[KO] requests not found")
        fail = True
    try:
        import matplotlib
        # prints the name and version of the package
        print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__}) "
              "- Data Visualization ready")
    except ImportError:
        print("[KO] matplotlib not found")
        fail = True

    if fail:
        print('Use "pip install -r requirements.txt" or "poetry install"'
              ' to install dependences')
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    try:
        # attempts to access the World Bank API
        try:
            response = requests.get("https://api.worldbank.org/v2/country\
/WLD/indicator/SP.POP.TOTL?format=json&per_page=20000&date=1960:2024")
        except Exception as e:
            print('\nConnection error:\n')
            print(e)
            sys.exit(1)

        # take what you got from the API and format it
        data = response.json()[1]
        data_format = [{'year': item.get('date'),
                        'population': item.get('value')}
                       for item in data]
        data_format = sorted(data_format, key=support)

        # processes the data using pandas
        print(f'Processing {len(data_format)} data points...')
        processed = pandas.DataFrame(data_format)

        # create a graph
        print("Generating visualization...")
        processed.plot(kind='line',
                       title="matrix_analysis",
                       xlabel='years',
                       ylabel='population',
                       x='year'
                       )

        # save the graph
        matplotlib.pyplot.savefig("matrix_analysis.png")
    except Exception as e:
        print(e)
        sys.exit(1)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
