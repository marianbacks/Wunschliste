{
 "cells": [
  {
   "cell_type": "code",
   "id": "9c515243-28aa-436d-bd68-acf8afc47018",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Lade die Excel-Datei\n",
    "def load_excel_file():\n",
    "    file_path = 'C:/Users/maria/Documents/Wunschliste.xlsx'  # Pfad zur Excel-Datei\n",
    "    df = pd.read_excel(file_path, header=1)  # Entferne oberste Zeile\n",
    "    return df\n",
    "\n",
    "# Streamlit-App erstellen\n",
    "def main():\n",
    "    st.title(\"Wunschliste Marian\")  # Titel der App\n",
    "\n",
    "    # Lade Daten\n",
    "    df = load_excel_file()\n",
    "\n",
    "    # Zeige die Tabelle mit klickbaren Links\n",
    "    st.write(\"Hier ist die Tabelle mit den gewünschten Einträgen:\")\n",
    "    for i in range(len(df)):\n",
    "        if pd.notna(df.iloc[i, 3]):  # Falls die vierte Spalte Links enthält\n",
    "            link = df.iloc[i, 3]\n",
    "            df.iloc[i, 3] = f\"[{link}]({link})\"\n",
    "\n",
    "    st.table(df)  # Zeige die Tabelle in der App\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:learnpy] *",
   "language": "python",
   "name": "conda-env-learnpy-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.20"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
