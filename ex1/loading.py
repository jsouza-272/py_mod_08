import sys


def support(item: dict) -> int:
    return item.get('year')


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    fail = False
    try:
        import pandas
        print(f"[OK] {pandas.__name__} ({pandas.__version__}) "
              "- Data manipulation ready")
    except ImportError:
        print("[KO] pandas not found")
        fail = True
    try:
        import requests
        print(f"[OK] {requests.__name__} ({requests.__version__}) "
              "- Network access ready")
    except ImportError:
        print("[KO] requests not found")
        fail = True
    try:
        import matplotlib
        print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__}) "
              "- Data Visualization ready")
    except ImportError:
        print("[KO] matplotlib not found")
        fail = True

    if fail:
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    try:
        response = requests.get("https://api.worldbank.org/v2/country\
/WLD/indicator/SP.POP.TOTL?format=json&per_page=20000&date=1980:2024")

        if response.status_code != 200:
            print(f"Connction failed: (status code={response.status_code})")
            sys.exit(1)
        data = response.json()[1]
        data_format = [{'year': item.get('date'),
                        'population': item.get('value')}
                       for item in data]

        print(f'Processing {len(data_format)} data points...')
        data_format = sorted(data_format, key=support)
        processed = pandas.DataFrame(data_format)

        print("Generating visualization...")
        processed.plot(kind='line',
                       title="matrix_analysis",
                       xlabel='years',
                       ylabel='population',
                       x='year'
                       )

        matplotlib.pyplot.savefig("matrix_analysis.png")
    except Exception as e:
        print(e)
        sys.exit(1)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
