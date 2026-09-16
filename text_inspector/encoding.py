from charset_normalizer import from_bytes


class EncodingCheck:

    @staticmethod
    def check(df):
        supported = df[
            df["supported"]
        ].copy()

        encodings = []

        for _, row in supported.iterrows():
            file = row["file"]

            try:
                with open(file, "rb") as f:
                    raw = f.read(65536)

                result = from_bytes(raw).best()

                if result is not None:
                    encoding = result.encoding

                else:
                    encoding = "Unknown"

            except Exception:
                encoding = "Error"

            encodings.append(encoding)

        supported["encoding"] = encodings

        print("\nEncoding Distribution")
        print("-" * 25)

        distribution = (
            supported["encoding"]
            .value_counts()
            .to_dict()
        )

        for encoding, count in distribution.items():
            print(
                f"{encoding}: {count}"
            )

        return supported