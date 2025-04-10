import os
import camelot
import pypdfium2 as ppdf  # type: ignore


class GetPDF:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.tables = None
        self.dataframes = None

    def extract_tables(self, pages="all", flavor="lattice"):
        try:
            self.tables = camelot.read_pdf(
                self.pdf_path,
                pages=pages,
                flavor=flavor,
            )
            return self.tables
        except Exception as e:
            print(f"Error extracting tables: {e}")
            return None

    def convert_tables_to_dataframes(self):
        if self.tables is None:
            print("No tables have been extracted. Run extract_tables() first.")
            return None

        self.dataframes = [table.df for table in self.tables]
        return self.dataframes

    def save_tables_to_csv(self, output_dir="./output"):
        os.makedirs(output_dir, exist_ok=True)

        if self.dataframes is None:
            self.convert_tables_to_dataframes()

        saved_files = []
        for i, df in enumerate(self.dataframes, 1):
            file_path = os.path.join(output_dir, f"table_{i}.csv")
            df.to_csv(file_path, index=False)
            saved_files.append(file_path)

        print(f"Saved {len(saved_files)} tables to {output_dir}")
        return saved_files

    def preview_pdf_page(self, page_number=0, output_path="preview.png"):
        try:
            pdf = ppdf.PdfDocument(self.pdf_path)

            renderer = pdf.render_topil(page_number)
            renderer.save(output_path)

            print(f"Preview saved to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error creating PDF preview: {e}")
            return None


def main():
    pdf_path = "seu_arquivo.pdf"

    pdf_extractor = GetPDF(pdf_path)

    tables = pdf_extractor.extract_tables()
    print(tables)

    dataframes = pdf_extractor.convert_tables_to_dataframes()
    print(dataframes)

    pdf_extractor.save_tables_to_csv()

    pdf_extractor.preview_pdf_page()


if __name__ == "__main__":
    main()
