
import random




def make_random_model(json_params = None , model_id = None , model_to = None):
    model_dict = {'model_id' : None,
                'model_score' : None,
                'class': None,
                'model_to' : None,
                'to_id' : None
                }

    model_dict['model_id'] = model_id
    model_dict['model_score'] = round( random.uniform(0, 1) , 4)
    model_dict['model_to'] = model_to
    
    if model_to == 'message_id':
        model_dict['to_id'] = json_params['message_id']
    elif model_to == 'dialog_id':
        model_dict['to_id'] = json_params['dialog_id']
    elif model_to == 'participants_id':
        model_dict['to_id'] = json_params['participants_id']
    elif model_to == 'user_id':
        model_dict['to_id'] = json_params['user_id']

    if(model_dict['model_score'] > 0):
        model_dict['class'] = 'Положительный'
    else:
        model_dict['class'] = 'Отрицательный'

    return model_dict

