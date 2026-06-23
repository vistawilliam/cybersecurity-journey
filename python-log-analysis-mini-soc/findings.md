# SOC Analysis Findings

## Summary

The Python log-analysis script processed the sample authentication log and identified repeated failed login activity from two IP addresses.

## Login Activity

* Successful logins: `3`
* Failed logins: `7`

## Suspicious IP Addresses

| IP Address      | Failed Attempts | Alert Status |
| --------------- | --------------: | ------------ |
| `45.33.12.80`   |               3 | Suspicious   |
| `103.21.244.50` |               4 | Suspicious   |

## Analysis

Both IP addresses exceeded the alert threshold of three failed login attempts. Repeated failed authentication attempts can indicate password guessing, brute-force activity, or unauthorized access attempts.

## Recommended SOC Actions

1. Review whether either IP address is known or expected.
2. Check whether successful logins occurred after the failed attempts.
3. Block or rate-limit repeated failed authentication attempts where appropriate.
4. Investigate the affected user accounts and reset credentials if compromise is suspected.

## Conclusion

This mini investigation demonstrates how basic Python scripting can support SOC monitoring by identifying repeated failed logins and prioritizing suspicious IP addresses for review.

> Note: The log data in this project is simulated for educational purposes.
