class FormatCheck:

    SUPPORTED_FORMATS = {
        ".txt",
        ".csv",
        ".json",
        ".jsonl",
        ".xml",
        ".md",
        ".tsv",
        ".yaml",
        ".yml"
    }

    @staticmethod
    def check(df):
        formats = (
            df["format"]
            .value_counts()
            .to_dict()
        )

        print("\nFormat Distribution")
        print("-" * 20)

        for ext, count in formats.items():
            print(f"{ext}: {count}")

        return formats

    @staticmethod
    def supported(df):
        supported = df[
            df["supported"]
        ]

        print(
            f"\nSupported files: {len(supported)}"
        )

        return supported

    @staticmethod
    def unsupported(df):
        unsupported = df[
            ~df["supported"]
        ]

        print(
            f"\nUnsupported files: "
            f"{len(unsupported)}"
        )

        if not unsupported.empty:

            distribution = (
                unsupported["format"]
                .value_counts()
                .to_dict()
            )

            print(
                "\nUnsupported Format Distribution"
            )

            print("-" * 30)

            for ext, count in distribution.items():
                print(
                    f"{ext}: {count}"
                )

        return unsupported