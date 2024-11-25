import logging
from unittest import TestCase
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(TestCase):
    def test_walk(self):
        try:
            runner = Runner("TestRunner1", speed=-5)
            self.assertEqual(runner.distance, 140)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(2)
            self.assertEqual(runner.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == "__main__":
    unittest.main()