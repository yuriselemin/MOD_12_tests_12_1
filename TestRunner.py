from MOD_12_tests_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Emily')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner2 = Runner('James')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = Runner('Lily')
        runner4 = Runner('Michael')
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)

if __name__ == '__main__':
    unittest.main()


