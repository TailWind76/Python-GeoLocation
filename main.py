from geopy.geocoders import Nominatim

def get_location_by_ip(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")  # Укажите своего агента пользователя
    location = geolocator.geocode(ip_address)
    return location

if __name__ == "__main__":
    ip_address = input("Введите IP-адрес для определения местоположения: ")
    location = get_location_by_ip(ip_address)
    if location:
        print(f"Местоположение для IP-адреса {ip_address}:")
        print(f"Широта: {location.latitude}, Долгота: {location.longitude}")
        print(f"Страна: {location.address}")
    else:
        print("Местоположение не найдено.")
