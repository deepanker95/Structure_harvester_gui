import os
import sys
import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from PIL import Image
from structureHarvester import run_harvester

def resource_path(relative_path):
    print(f"Resolving path for: {relative_path}")
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)

REQUIRED_FILES = ["structureHarvester.py", "harvesterCore.py"]

class StructureHarvesterGUI:
    def __init__(self, root):
        print("Initializing StructureHarvesterGUI...")
        try:
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            print("Customtkinter appearance set.")

            self.root = root
            self.root.title("Structure Harvester GUI")
            self.root.geometry("650x750")
            self.root.resizable(True, True)
            print("Root window configured.")

            self.input_dir_label = ctk.CTkLabel(root, text="Select Input Directory:")
            self.input_dir_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            self.input_dir_entry = ctk.CTkEntry(root, width=300)
            self.input_dir_entry.grid(row=0, column=1, padx=10, pady=5)

            self.browse_input_button = ctk.CTkButton(root, text="Browse", command=self.browse_input_dir)
            self.browse_input_button.grid(row=0, column=2, padx=10, pady=5)

            self.output_dir_label = ctk.CTkLabel(root, text="Select Output Directory:")
            self.output_dir_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            self.output_dir_entry = ctk.CTkEntry(root, width=300)
            self.output_dir_entry.grid(row=1, column=1, padx=10, pady=5)

            self.browse_output_button = ctk.CTkButton(root, text="Browse", command=self.browse_output_dir)
            self.browse_output_button.grid(row=1, column=2, padx=10, pady=5)

            self.run_button = ctk.CTkButton(root, text="Run Structure Harvester", command=self.run_structure_harvester)
            self.run_button.grid(row=4, column=0, columnspan=3, pady=20)

            self.evanno_var = ctk.BooleanVar()
            self.evanno_checkbox = ctk.CTkCheckBox(root, text="Perform Evanno Method", variable=self.evanno_var)
            self.evanno_checkbox.grid(row=2, column=0, columnspan=3, pady=5)

            self.clumpp_var = ctk.BooleanVar()
            self.clumpp_checkbox = ctk.CTkCheckBox(root, text="Generate CLUMPP Files", variable=self.clumpp_var)
            self.clumpp_checkbox.grid(row=3, column=0, columnspan=3, pady=5)

            self.log_text = ctk.CTkTextbox(root, height=300, width=500, state="disabled")
            self.log_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

            self.extract_button = ctk.CTkButton(root, text="Extract Tables", command=self.extract_tables)
            self.extract_button.grid(row=6, column=0, columnspan=3, pady=10)

            self.plot_button = ctk.CTkButton(root, text="Generate Plots", command=self.generate_plots)
            self.plot_button.grid(row=7, column=0, columnspan=3, pady=10)

            try:
                logo_path = resource_path("logo.png")
                print(f"Looking for logo at: {logo_path}")
                if os.path.exists(logo_path):
                    logo_image = Image.open(logo_path)
                    logo_ctk_image = ctk.CTkImage(light_image=logo_image, size=(170, 170))
                    logo_label = ctk.CTkLabel(root, image=logo_ctk_image, text="")
                    logo_label.grid(row=0, column=0, columnspan=3, pady=10)
                    logo_label.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-35)
                    print("Logo loaded successfully.")
                else:
                    print(f"Error: 'logo.png' not found at {logo_path}")
            except Exception as e:
                print(f"Error loading logo: {e}")

            self.credit_label = ctk.CTkLabel(root, text="Developed by Deepanker Das & Devojit Sarma", font=("Arial", 10, "italic"))
            self.credit_label.grid(row=9, column=0, columnspan=3, pady=10)
            print("GUI components initialized.")

        except Exception as e:
            print(f"Error in __init__: {e}")
            raise

    def browse_input_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir_entry.delete(0, ctk.END)
            self.input_dir_entry.insert(0, directory)

    def browse_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_entry.delete(0, ctk.END)
            self.output_dir_entry.insert(0, directory)

    def ensure_files(self):
        missing_files = []
        for file in REQUIRED_FILES:
            file_path = resource_path(file)
            print(f"Checking for required file: {file_path}")
            if not os.path.isfile(file_path):
                missing_files.append(file)
        if missing_files:
            self.log(f"Required files are missing: {', '.join(missing_files)}. Please ensure they are included in the app bundle.")
            return False
        return True

    def run_structure_harvester(self):
        input_dir = self.input_dir_entry.get()
        output_dir = self.output_dir_entry.get()

        if not os.path.isdir(input_dir):
            messagebox.showerror("Error", "Invalid input directory!")
            return

        if not os.path.isdir(output_dir):
            messagebox.showerror("Error", "Invalid output directory!")
            return

        if not self.ensure_files():
            messagebox.showerror("Error", "Required files are missing.")
            return

        self.log("Running Structure Harvester...")
        try:
            result = run_harvester(
                input_dir=input_dir,
                output_dir=output_dir,
                evanno=self.evanno_var.get(),
                clumpp=self.clumpp_var.get()
            )
            self.log("Structure Harvester completed successfully.")
            self.log(result)
        except Exception as e:
            self.log(f"Error occurred while running Structure Harvester: {e}")

    def extract_tables(self):
        output_dir = self.output_dir_entry.get()
        summary_path = os.path.join(output_dir, "summary.txt")
        evanno_path = os.path.join(output_dir, "evanno.txt")
        try:
            self.log("Extracting tables from summary.txt...")
            summary_tables = self.extract_tables_from_file(summary_path)
            self.log(f"Extracted {len(summary_tables)} tables from summary.txt.")
            self.log("Extracting table from evanno.txt...")
            evanno_table = self.extract_evanno_table(evanno_path)
            self.log("Extracted 1 table from evanno.txt.")
            for idx, table in enumerate(summary_tables):
                output_file = os.path.join(output_dir, f"summary_table_{idx + 1}.csv")
                table.to_csv(output_file, index=False)
                self.log(f"Summary Table {idx + 1} saved to {output_file}.")
            if not evanno_table.empty:
                output_file = os.path.join(output_dir, "evanno_table.csv")
                evanno_table.to_csv(output_file, index=False)
                self.log(f"Evanno Table saved to {output_file}.")
        except Exception as e:
            self.log(f"Error extracting tables: {e}")

    def extract_tables_from_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                lines = [line.strip() for line in f.readlines()]
            def find_table(lines, start_marker="##########", end_marker=""):
                start_idx, end_idx = None, None
                for i, line in enumerate(lines):
                    if line.startswith(start_marker):
                        start_idx = i + 1
                    elif start_idx is not None and line == end_marker:
                        end_idx = i
                        break
                return start_idx, end_idx
            t1_start, t1_end = find_table(lines)
            table1_lines = lines[t1_start:t1_end] if t1_start and t1_end else []
            t2_start, t2_end = find_table(lines[t1_end:], start_marker="##########")
            table2_lines = lines[t2_start + t1_end:t2_end + t1_end] if t2_start and t2_end else []
            table1 = pd.read_csv(StringIO('\n'.join(table1_lines)), sep="\t") if table1_lines else pd.DataFrame()
            table2 = pd.read_csv(StringIO('\n'.join(table2_lines)), sep="\t") if table2_lines else pd.DataFrame()
            return [table1, table2] if not table1.empty or not table2.empty else []
        except Exception as e:
            raise Exception(f"Error reading file {file_path}: {e}")

    def extract_evanno_table(self, file_path):
        try:
            with open(file_path, "r") as f:
                lines = [line.strip() for line in f]
            start_idx = None
            header = None
            for i, line in enumerate(lines):
                if line.startswith("# K"):  # Matches '# K\tReps\tMean LnP(K)...'
                    start_idx = i
                    header = line.lstrip('# ').split('\t')  # Remove '#' and split by tabs
                    break
            if start_idx is None or header is None:
                self.log("Evanno table marker or header not found.")
                return pd.DataFrame()
            table_data = "\n".join([line for line in lines[start_idx + 1:] if line])
            # Replace 'NA' with NaN for pandas compatibility
            table_data = table_data.replace("NA", "NaN")
            df = pd.read_csv(StringIO(table_data), sep="\t", names=header)
            return df
        except Exception as e:
            self.log(f"Error extracting Evanno table: {e}")
            return pd.DataFrame()

    def generate_plots(self):
        output_dir = self.output_dir_entry.get()
        summary_file = os.path.join(output_dir, "summary_table_1.csv")
        evanno_file = os.path.join(output_dir, "evanno_table.csv")
        try:
            summary_df = pd.read_csv(summary_file)
            plt.figure(figsize=(10, 6))
            plt.errorbar(summary_df['# K'], summary_df['mean est. LnP(Data)'], yerr=summary_df['stdev est. LnP(Data)'], fmt='o', color='blue', ecolor='gray', capsize=4, label='Mean LnP(K) ± SD')
            plt.title('Mean Likelihood L(K) ± SD per K Value', fontsize=14)
            plt.xlabel('K (Number of Clusters)', fontsize=12)
            plt.ylabel('Mean LnP(K)', fontsize=12)
            plt.xticks(summary_df['# K'])
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.legend()
            plot1_path = os.path.join(output_dir, "lnp_k_plot.png")
            plt.tight_layout()
            plt.savefig(plot1_path)
            self.log(f"LnP(K) ± SD plot saved to {plot1_path}.")
            plt.close()
            evanno_df = pd.read_csv(evanno_file)
            plt.figure(figsize=(8, 6))
            plt.plot(evanno_df['K'], evanno_df['Delta K'], marker='o', color='r')
            plt.title("Delta K vs. K")
            plt.xlabel("K (Number of Clusters)")
            plt.ylabel("Delta K")
            plot2_path = os.path.join(output_dir, "delta_k_plot.png")
            plt.savefig(plot2_path)
            self.log(f"Delta K vs. K plot saved to {plot2_path}.")
            plt.close()
            plt.figure(figsize=(8, 6))
            plt.plot(evanno_df['K'], evanno_df["Ln'(K)"], marker='o', color='b')
            plt.title("Rate of Change of Likelihood Distribution")
            plt.xlabel("K (Number of Clusters)")
            plt.ylabel("Ln'(K)")
            plot3_path = os.path.join(output_dir, "rate_of_change_plot.png")
            plt.savefig(plot3_path)
            self.log(f"Rate of Change plot saved to {plot3_path}.")
            plt.close()
            plt.figure(figsize=(8, 6))
            plt.plot(evanno_df['K'], evanno_df["|Ln''(K)|"], marker='o', color='orange')
            plt.title("2nd Order Rate of Change of Likelihood Distribution")
            plt.xlabel("K (Number of Clusters)")
            plt.ylabel("|Ln''(K)|")
            plot4_path = os.path.join(output_dir, "second_order_rate_of_change_plot.png")
            plt.savefig(plot4_path)
            self.log(f"2nd Order Rate of Change plot saved to {plot4_path}.")
            plt.close()
        except Exception as e:
            self.log(f"Error generating plots: {e}")

    def log(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert(ctk.END, message + "\n")
        self.log_text.configure(state="disabled")
        self.log_text.see(ctk.END)

if __name__ == "__main__":
    print("Starting application...")
    try:
        root = ctk.CTk()
        print("CTk root created.")
        app = StructureHarvesterGUI(root)
        print("App instance created.")
        root.mainloop()
        print("Mainloop exited.")
    except Exception as e:
        print(f"Error in main: {e}")
        raise