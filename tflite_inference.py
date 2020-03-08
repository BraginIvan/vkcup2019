from tflite_runtime.interpreter import Interpreter
import numpy as np

def apply(tflite_path, in0, in1, in2):
    interpreter = Interpreter(model_path=tflite_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_tensor0 = input_details[0]['index']
    input_tensor1 = input_details[1]['index']
    input_tensor2 = input_details[2]['index']
    output_tensors = [tensor['index'] for tensor in output_details]

    res1 = []
    res2 = []
    res3 = []
    for line0,line1,line2 in zip(in0.values, in1.values, in2.values):
        line_res1 = []
        line_res2 = []
        line_res3 = []
        interpreter.set_tensor(input_tensor0, np.array([line0]).astype(input_details[0]['dtype']))
        interpreter.set_tensor(input_tensor1, np.array([line1]).astype(input_details[1]['dtype']))
        interpreter.set_tensor(input_tensor2, np.array([line2]).astype(input_details[1]['dtype']))
        interpreter.invoke()
        for t in output_tensors:
            a = interpreter.get_tensor(t)
            line_res1.append(a[0][0])
            line_res2.append(a[0][1])
            line_res3.append(a[0][2])
        res1.append(np.median(line_res1))
        res2.append(np.median(line_res2))
        res3.append(np.median(line_res3))
    return res1, res2, res3



