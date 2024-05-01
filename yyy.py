import os

# Path to the test novels folder
novels_folder_path = r'D:\Gethub\SummaryFlow\TestNovels'

# List the files in the test novels folder
novels = os.listdir(novels_folder_path)

# Path to the test summaries folder
summaries_folder_path = r'D:\Gethub\SummaryFlow\TestSummaries'

# List the files in the test summaries folder
summaries = os.listdir(summaries_folder_path)

all_novels = []
all_summaries = []

# Loop through the novels
for file_name in novels:
    # Read the novels
    if file_name.endswith('.txt'):
        with open(os.path.join(novels_folder_path, file_name), 'r', encoding='utf-8') as file:
            novel_content = file.read()
            all_novels.append(novel_content)
            
# Loop through the summaries
for file_name in summaries:
    # Read the summaries
    if file_name.endswith('.txt'):
        with open(os.path.join(summaries_folder_path, file_name), 'r', encoding='utf-8') as file:
            summary_content = file.read()
            all_summaries.append(summary_content)

# Loop through the novels
for i in range(len(all_novels)):
    print('novels content')
    print(all_novels[i])
    print('summaries content')
    print(all_summaries[i])