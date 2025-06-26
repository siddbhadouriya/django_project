import requests
import datetime
from myapp.models import CowinData  # Make sure to import your model

def get_cowin_data_by_pincode(pincode):
    try:
        current_date = datetime.date.today().strftime('%d-%m-%Y')
        url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={current_date}'
        
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        sessions = data.get("sessions", [])

        for session in sessions:
            if session.get('available_capacity', 0) > 0:
                CowinData.objects.create(
                    center_id=session.get('center_id'),
                    name=session.get('name'),
                    state=session.get('state_name'),
                    pincode=session.get('pincode'),
                    fee_type=session.get('fee_type'),
                    fee=int(session.get('fee', 0)),
                    available_capacity=session.get('available_capacity'),
                    available_capacity_dose1=session.get('available_capacity_dose1'),
                    available_capacity_dose2=session.get('available_capacity_dose2'),
                    min_age_limit=session.get('min_age_limit'),
                    vaccine=session.get('vaccine')
                )

        print("Data inserted successfully.")
        print(data)
        return data

    except Exception as e:
        print("Error:", e)
        return None

# Call the function
get_cowin_data_by_pincode(226020)


