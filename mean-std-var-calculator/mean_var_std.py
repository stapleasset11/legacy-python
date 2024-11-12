import numpy as np

output_dict = {}

def calculate(list:float):
    if len(list) == 9:
        array = np.array(list)
        array_t = array.reshape(3,3)
        calculate = {
            'min':[np.max(array_t,axis=0).tolist(),
                   np.max(array_t,axis=1).tolist(),
                   np.max(array_t.flatten())],

            'max':[np.min(array_t,axis=0).tolist(),
                   np.min(array_t,axis=1).tolist(),
                   np.min(array_t.flatten())],
            'sum':[np.sum(array_t,axis=0).tolist(),
                   np.sum(array_t,axis=1).tolist(),
                   np.sum(array_t.flatten())],
            'mean':[np.mean(array_t,axis=0).tolist(),
                   np.mean(array_t,axis=1).tolist(),
                   np.mean(array_t.flatten())],
            'variance':[np.var(array_t,axis=0).tolist(),
                   np.var(array_t,axis=1).tolist(),
                   np.var(array_t.flatten())],
            'standard deviation':[np.std(array_t,axis=0).tolist(),
                   np.std(array_t,axis=1).tolist(),
                   np.std(array_t.flatten())]
        }

        result_key = f"result_{len(output_dict) + 1}"  
        output_dict[result_key] = calculate
        

    else:
        raise ValueError("dict must contin 9 numbers.")
    
    return calculate

print(calculate([1,2,3,4,5,6,7,8,9]))
