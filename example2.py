from time import sleep
import tellopy


def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)


def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(5)
        drone.up(30)
        sleep(1)
        drone.up(0)

	sleep(3)
	drone.flip_forwardright()
	sleep(3)

	drone.forward(40)
	sleep(1)
	drone.forward(0)

	drone.clockwise(50)
	sleep(5)
        drone.clockwise(0)

	sleep(1)
	drone.right(40)
	sleep(2)
	drone.right(0)
	sleep(1)
	drone.left(40)
	sleep(2)
	drone.left(0)

	sleep(1)
	drone.forward(30)
	drone.down(20)
	sleep(2)
	drone.forward(0)
	sleep(1)

	drone.counter_clockwise(50)
	sleep(5)
        drone.counter_clockwise(0)

        drone.land()
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
