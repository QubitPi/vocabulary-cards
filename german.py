import yaml
from string import Template

if __name__ == "__main__":
    with open("german.yaml", 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Error reading YAML file: {e}")

    vocabulary_file_references = []
    for vocabulary in data:
        word = vocabulary["term"]

        audio = vocabulary["audio"]

        definitions = vocabulary["definition"]
        if isinstance(definitions, str):
            definitions = [definitions]
        try:
            with open("german-template.tex", 'r') as template_file:
                template_content = template_file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template file not found: german-template.tex")

        declension = vocabulary["declension"]

        # change proper entry font to German
        for row_idx, row in enumerate(declension):
            if row_idx == 0:
                continue
            for col_idx, col in enumerate(row):
                if col_idx == 0 or declension[row_idx][col_idx] == "N/A":
                    continue
                declension[row_idx][col_idx] = "{\German " + declension[row_idx][col_idx] + "}"

        declension_table = [" & ".join([item for item in row]) for row in declension]
        for idx, row in enumerate(declension_table):
            if idx == 0:
                declension_table[idx] += " \\\\\\hline\\hline"
            elif idx == len(declension_table) - 1:
                declension_table[idx] += " \\\\"
            else:
                declension_table[idx] += " \\\\\\hline"



        template = Template(template_content)
        substituted_content = template.substitute({
            "word": word,
            "audio": audio,
            "definitions": "\n".join([f"    \item {definition}" for definition in definitions]),
            "declension_table_rows": "\n".join(declension_table)
        })

        try:
            with open("german/" + word + ".tex", 'w') as output_file:
                output_file.write(substituted_content)
        except Exception as e:
            raise Exception(f"Error writing to output file: {word}. {e}")

        vocabulary_file_references.append("german/" + word)

    with open("german.tex", 'r') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1

    for i, line in enumerate(lines):
        if "VOCABULARY-START" in line:
            start_index = i
        if "VOCABULARY-END" in line:
            end_index = i
            break

    if start_index == -1 or end_index == -1 or start_index >= end_index:
        raise Exception(f"Missing VOCABULARY-START/VOCABULARY-END comment in german.tex")

    updated_lines = lines[:start_index + 1]
    updated_lines.append("\n".join([f"    \input{ {reference} }".replace("'", "") for reference in vocabulary_file_references]))
    updated_lines.append("\n")
    updated_lines.extend(lines[end_index:])

    with open("german.tex", 'w') as file:
        file.writelines(updated_lines)