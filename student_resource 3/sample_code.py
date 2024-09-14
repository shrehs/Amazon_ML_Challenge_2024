import os
import random
import pandas as pd

def predictor(image_link, category_id, entity_name):
    '''
    Call your model/approach here
    '''
    #TODO
    return "" if random.random() > 0.5 else "10 inch"

if __name__ == "__main__":
    DATASET_FOLDER = 'C:/Users/User/Amazon_ML_Challenge_2024/student_resource 3/dataset'
    
    # Load the test dataset
    try:
        test = pd.read_csv(os.path.join(DATASET_FOLDER, 'test.csv'))
    except FileNotFoundError:
        print(f"File not found: {os.path.join(DATASET_FOLDER, 'test.csv')}")
        exit(1)

    # Ensure required columns are present
    required_columns = ['image_link', 'group_id', 'entity_name']
    if not all(col in test.columns for col in required_columns):
        print(f"Missing columns in the input data. Required columns are: {required_columns}")
        exit(1)
    
    # Apply the predictor function
    test['prediction'] = test.apply(
        lambda row: predictor(row['image_link'], row['group_id'], row['entity_name']), axis=1)
    
    # Save the predictions to a CSV file
    output_filename = os.path.join(DATASET_FOLDER, 'test_out.csv')
    try:
        test[['index', 'prediction']].to_csv(output_filename, index=False)
        print(f"Predictions saved to: {output_filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")