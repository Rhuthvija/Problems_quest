class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            # Collision is possible
            while stack and stack[-1] > 0 and asteroid < 0:

                if stack[-1] < -asteroid:
                    # Stack asteroid explodes
                    stack.pop()

                elif stack[-1] == -asteroid:
                    # Both explode
                    stack.pop()
                    break

                else:
                    # Current asteroid explodes
                    break

            else:
                # No collision / current asteroid survives
                stack.append(asteroid)

        return stack