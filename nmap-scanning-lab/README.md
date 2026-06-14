# Nmap Scanning Lab

## Objective

This lab demonstrates basic network scanning using Nmap in a safe local environment.

## Tools Used

* Windows Command Prompt
* Nmap 7.99
* GitHub for documentation

## Target

The scan target used in this lab is:

```text
localhost
```

This means the scans were performed against my own machine.

## Scan 1: Basic Nmap Scan

### Command Used

```cmd
nmap localhost
```

### Purpose

This scan checks the most common ports on the local machine and identifies whether any ports are open, closed, or filtered.

### Screenshot

![Basic Localhost Scan](screenshots/localhost-basic-scan.png)

## Scan 2: Service Version Detection

### Command Used

```cmd
nmap -sV localhost
```

### Purpose

The `-sV` option attempts to detect the service and version running on open ports.

### Screenshot

![Service Version Scan](screenshots/localhost-service-scan.png)

## Nmap Version

The installed Nmap version was verified using:

```cmd
nmap --version
```

### Screenshot

![Nmap Version](screenshots/nmap-version.png)

## What I Learned

* How to verify Nmap installation
* How to scan a local machine safely
* How to identify open ports
* How service detection works using `-sV`
* Why documentation is important in cybersecurity work

## Notes

This lab was performed only on my own system for learning and documentation purposes.
