import os
import glob

def count_lines_in_pas_files(directory):
    total_lines = 0
    # پیدا کردن تمام فایل‌های .pas در پوشه
    pas_files = glob.glob(os.path.join(directory, '*.pas'))
    
    for pas_file in pas_files:
        with open(pas_file, 'r', encoding='utf-8') as file:
            # شمارش تعداد خطوط هر فایل
            lines = file.readlines()
            total_lines += len(lines)
    
    return total_lines

# مسیر پوشه‌ی مورد نظر
directory_path = 'C:\\Users\\Amir\\Downloads\\Compressed\\freeship-plus-in-lazarus-master\\Forms'

# فراخوانی تابع و چاپ نتیجه
total_lines = count_lines_in_pas_files(directory_path)
print(f'Total lines in .pas files: {total_lines}')
