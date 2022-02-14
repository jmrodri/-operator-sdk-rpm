# operator-sdk-rpm

This is a repo to work on packaging [operator-sdk][operator-sdk] as an RPM.

## Interested?
If you want to help or learn there are some pre-requisites:

* Fedora machine
* Install `rpm-devel`, `rpm-build`, `mock`, `wget` and optionally `fedpkg`

```
$ rpm -q mock fedpkg rpm-build rpm-devel
mock-2.15-1.fc35.noarch
fedpkg-1.41-2.fc35.noarch
rpm-build-4.17.0-4.fc35.x86_64
rpm-devel-4.17.0-4.fc35.x86_64
```

You will also need to download the latest [operator-sdk][operator-sdk] tarball.
I've provided a simple script `get_tarball.sh` that you can run to download the
`operator-sdk` source in tar format. The script uses `wget` which is why it was
a pre-requisite package.

Here's what you should see.

```
$ ./get_tarball.sh
--2022-02-14 10:17:47--  https://github.com/operator-framework/operator-sdk/archive/refs/tags/v1.17.0.tar.gz
Resolving github.com (github.com)... 140.82.112.4
Connecting to github.com (github.com)|140.82.112.4|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/operator-framework/operator-sdk/tar.gz/refs/tags/v1.17.0 [following]
--2022-02-14 10:17:47--  https://codeload.github.com/operator-framework/operator-sdk/tar.gz/refs/tags/v1.17.0
Resolving codeload.github.com (codeload.github.com)... 140.82.114.9
Connecting to codeload.github.com (codeload.github.com)|140.82.114.9|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2470000 (2.4M) [application/x-gzip]
Saving to: ‘v1.17.0.tar.gz’

v1.17.0.tar.gz                                  100%[=====================================================================================================>]   2.36M  10.3MB/s    in 0.2s

2022-02-14 10:17:48 (10.3 MB/s) - ‘v1.17.0.tar.gz’ saved [2470000/2470000]
```

## Additional reading
* [Fedora Go Packaging Guidelines][fedora-go-guidelines]

[operator-sdk]: https://github.com/operator-framework/operator-sdk
[fedora-go-guidelines]: https://docs.fedoraproject.org/en-US/packaging-guidelines/Golang/
[sdk-117]: https://github.com/operator-framework/operator-sdk/archive/refs/tags/v1.17.0.tar.gz
