"""
Difficulty: Hard

Topics: Minimum Difficulty of a Job Schedule

Summary:
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
"""

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        length = len(jobDifficulty)
        if d > length:
            return -1
        min_difficulties = [[float('inf')] * length for _ in range(d)]
        max_diff = 0
        i = 0
        while i <= length - d:
            max_diff = max(max_diff, jobDifficulty[i])
            min_difficulties[0][i] = max_diff
            i += 1
        current_day = 1
        while current_day < d:
            to = current_day
            while to <= length - d + current_day:
                current_job_difficulty = jobDifficulty[to]
                result = float('inf')
                j = to - 1
                while j >= current_day - 1:
                    result = min(result, min_difficulties[current_day - 1][j] + current_job_difficulty)
                    current_job_difficulty = max(current_job_difficulty, jobDifficulty[j])
                    j -= 1
                min_difficulties[current_day][to] = result
                to += 1
            current_day += 1
        return min_difficulties[d - 1][length - 1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDifficulty(jobDifficulty=[1, 2, 3, 4, 5, 6], d=2))