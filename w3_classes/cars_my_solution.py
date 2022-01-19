import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if brand and carrying and photo_file_name and self.is_valid_photo(photo_file_name):
            self.brand = brand
            self.carrying = float(carrying)
            self.photo_file_name = photo_file_name
        else:
            raise ValueError

    @staticmethod
    def is_valid_photo(photo_file_name):
        extensions = ('.jpg', '.jpeg', '.png', '.gif')
        path, ext = os.path.splitext(photo_file_name)
        return path and ext in extensions

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = self.get_l_w_h(body_whl)
        self.car_type = 'truck'

    def get_l_w_h(self, body_whl):
        body_whl_list = body_whl.split('x')
        filtred_whl = []
        try:
            filtred_whl = [float(x) for x in body_whl_list if float(x) > 0]
        except:
            pass

        if len(filtred_whl) == 3:
            return filtred_whl
        else:
            return 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if extra:
            self.extra = extra
        else:
            raise ValueError
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row):
                car_type = row[0]
                try:
                    if car_type == 'car':
                        car_list.append(Car(row[1], row[3], row[5], row[2]))
                    elif car_type == 'truck':
                        car_list.append(Truck(row[1], row[3], row[5], row[4]))
                    elif car_type == 'spec_machine':
                        car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
                except ValueError:
                    pass
    return car_list
