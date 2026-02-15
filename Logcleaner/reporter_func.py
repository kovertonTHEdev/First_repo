from datetime import datetime


def get_report(report_file):
    try:
        with open(report_file, "r", encoding="UTF-8") as file:
            report_list = []
            for element in file:
                cleaned_element = element.strip()
                if not cleaned_element:
                    continue
                parts = cleaned_element.split(" | ")
                if len(parts) != 3:
                    continue
                text_date = parts[0]
                warning = parts[1]
                error = parts[2]
                try:
                    format_str = "%Y-%m-%d %H:%M:%S"
                    datetime_obj = datetime.strptime(text_date, format_str)
                    report_dict = {"DATE": datetime_obj, "STATUS": warning, "DESCRIPTION": error}
                    report_list.append(report_dict)
                except ValueError:
                    continue
    except FileNotFoundError:
        return[]
    valid_count = 0 
    level_counter = {}
    first_dt = None 
    last_dt = None 

    for record in report_list:
        valid_count += 1
        level = record["STATUS"]
        dt = record["DATE"]

        level_counter[level] = level_counter.get(level, 0) + 1

        if first_dt is None:
            first_dt = dt
        if last_dt is None:
            last_dt = dt
        if dt < first_dt:
            first_dt = dt
        if dt > last_dt:
            last_dt = dt
        
    if valid_count == 0:
        first_text = "N/A"
        last_text = "N/A"
    else:
        first_text = first_dt.strftime("%Y-%m-%d %H:%M:%S")
        last_text = last_dt.strftime("%Y-%m-%d %H:%M:%S")
    info = level_counter.get("INFO", 0)
    warning_inf = level_counter.get("WARNING", 0)
    error_inf = level_counter.get("ERROR", 0)
    result = [f"Total lines: {valid_count}, INFO: {info}, WARNING: {warning_inf}, ERROR: {error_inf}, First timestamp: {first_text}, Last timestamp: {last_text}"]
    full_result = "\n".join(result)

    return full_result