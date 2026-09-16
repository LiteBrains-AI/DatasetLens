from langdetect import detect
from langdetect import LangDetectException


class LanguageCheck:

    @staticmethod
    def check(df):
        supported = df[
            df["supported"]
        ].copy()

        languages = []

        for _, row in supported.iterrows():
            file = row["file"]

            try:
                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:
                    text = f.read(10000)

                if not text.strip():
                    language = "Empty"

                elif len(text.strip()) < 20:
                    language = "Too Short"

                else:
                    language = detect(text)

            except LangDetectException:
                language = "Unknown"

            except Exception:
                language = "Error"

            languages.append(language)

        supported["language"] = languages

        print("\nLanguage Distribution")
        print("-" * 25)

        distribution = (
            supported["language"]
            .value_counts()
            .to_dict()
        )

        for language, count in distribution.items():
            print(
                f"{language}: {count}"
            )

        return supported