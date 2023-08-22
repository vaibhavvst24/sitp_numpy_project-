import csv 
import numpy as np
data = []
with open(r"C:\Users\vaibh\Downloads\MER_T07_02A-2020-02-03.csv", 'r') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')
    for row in file_reader:
        data.append(row)

data = np.array(data) 

# Get the shape of the array
array_shape = data.shape

# Get the data type of the elements
data_type = data.dtype

# Get the number of dimensions
num_dimensions = data.ndim

# Get the total number of elements
num_elements = data.size

# Print the results
print("Array Shape:", array_shape)
print("Data Type:", data_type)
print("Number of Dimensions:", num_dimensions)
print("Number of Elements:", num_elements)

# Extract the data from the first 10 rows of the 4th column
data_subset = data[:10, 3]  # Assuming the 4th column is index 3 (0-based indexing)

# Print the extracted data
print("\nData in the first 10 rows of the 4th column:", data_subset)

# Get the first row of the array
header_row = data[0]

# Print the header row
print("\nHeader row:", header_row)

# Extract the data from columns 2 and 3, rows 1 to 20
data_subset = data[1:21, 1:3]  # Rows 1 to 20, Columns 2 and 3 (0-based indexing)

# Print the extracted data
print("\nData in columns 2 and 3, rows 1 to 20:")
print(data_subset)

# Extract the data from the first three and last three rows for all columns
selected_rows = np.concatenate((data[:3], data[-3:]), axis=0)

# Print the extracted data
print("\nData in the first three and last three rows of all columns:")
print(selected_rows)

# Identify the column index containing the net amount of electricity generated
net_amount_column_index = 2  # Adjust this index according to your data (0-based indexing)

# Get the indices that would sort the data based on the net amount column
sorted_indices = np.argsort(data[:, net_amount_column_index])

# Sort the entire data array based on the sorted indices
sorted_data = data[sorted_indices]

# Print the sorted data
print("\nData sorted based on net amount of electricity generated:")
print(sorted_data)

# Identify the column indices for coal and nuclear generation
coal_column_index = 4  # Adjust this index according to your data (0-based indexing)
nuclear_column_index = 5  # Adjust this index according to your data (0-based indexing)

# Function to convert date strings to integers
def date_string_to_int(date_string):
    return int(date_string[-1])  # Extract the year part

# Filter rows within the date range 1949-1990 and exclude non-numeric entries
valid_rows = []
for row in data:
    try:
        year = int(row[0][:4])
        if 1949 <= year <= 1990:
            coal = float(row[coal_column_index])
            nuclear = float(row[nuclear_column_index])
            valid_rows.append([coal, nuclear])
    except ValueError:
        pass

# Calculate the total electricity generation for coal and nuclear
total_coal_generation = np.sum([row[0] for row in valid_rows])
total_nuclear_generation = np.sum([row[1] for row in valid_rows])

# Print the results
print("\nTotal amount of electricity generated using coal between 1949-1990:", total_coal_generation)
print("Total amount of electricity generated using nuclear between 1949-1990:", total_nuclear_generation)

# Identify the column index for the energy source information
energy_source_column_index = 1  # Adjust this index according to your data (0-based indexing)

# Extract unique energy source values
unique_sources = np.unique(data[:, energy_source_column_index])

# Print the unique sources of energy generation
print("\nUnique sources of energy generation:")
print(unique_sources)

# Identify the column indices for energy source and energy type
energy_source_column_index = 1  # Adjust this index according to your data (0-based indexing)
energy_type_column_index = 2  # Adjust this index according to your data (0-based indexing)

# Define the energy source and energy type to filter
target_energy_source = 'Wind'
target_energy_type = 'Annual'

# Create a mask to filter the data
source_mask = data[:, energy_source_column_index] == target_energy_source
type_mask = data[:, energy_type_column_index] == target_energy_type
combined_mask = np.logical_and(source_mask, type_mask)

# Apply the mask to the data to get the filtered rows
filtered_data = data[combined_mask]

# Print the filtered details for Wind Energy (Annual)
print("\nDetails for Wind Energy (Annual):")
for row in filtered_data:
    print(', '.join(row))

# Identify the column index for the energy source
energy_source_column_index = 1  # Adjust this index according to your data (0-based indexing)

# Define the energy source for the USA
target_energy_source = 'Total Energy'

# Create a mask to filter the data for the USA's total energy
source_mask = data[:, energy_source_column_index] == target_energy_source

# Apply the mask to the data to get the filtered rows
filtered_data = data[source_mask]

# Calculate and print the total energy generated in the USA till date
total_energy_generated = np.sum(filtered_data[:, 2:].astype(float))  # Assuming energy generation columns start from index 2
print("\nTotal energy generated in the USA till date:", total_energy_generated)

# Extract the headers from the first row
headers = data[0]

# Find the indices of the columns containing annual energy generation data
annual_energy_indices = np.where(headers[2:] == 'Annual')[0] + 2  # Add 2 to account for skipping the first two columns

# Extract the years from the headers corresponding to annual energy columns
years = np.array([int(header[:4]) for header in headers[annual_energy_indices]])

# Extract the annual energy generation values
annual_energy_generation = data[1:, annual_energy_indices].astype(float)

if annual_energy_generation.size == 0:
    print("\nNo valid annual energy generation data found.")
else:
    # Find the index of the maximum annual energy generation
    max_index = np.unravel_index(np.argmax(annual_energy_generation, axis=None), annual_energy_generation.shape)

    # Get the year and value of the maximum annual energy generation
    max_year = years[max_index[0]]
    max_value = annual_energy_generation[max_index]

    print("The maximum annual energy was generated in the year:", max_year)
    print("The maximum annual energy generation value was:", max_value)

