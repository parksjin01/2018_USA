# 2018_USA
2018년 미국에서 진행한 프로젝트를 정리한 repository 입니다.

## 폴더 내용
> Log: 시나리오 시뮬레이션에서 나온 로그 파일을 모아놓은 폴더  
> Raw: Log 폴더에 들어 있는 파일들을 그래프를 그리기 위해 formatting 한 파일들을 모아놓은 그래프  
> Graph: 각각의 시나리오의 throughput 그래프와 SINR 그래프를 모아놓은 그래프  
> Block: 각각의 시나리오의 장애물, UE, eNB 의 배치를 시각화한 폴더  
> Modification: 서로 다른 ns3 버전의 호완성 문제를 수정해주고 설정 파일을 적절히 변경해주기 위한 수정파일이 들어있다.

## Integrate DCE + mmWave + MPTCP

### Official homepage for each program
- [DCE-1.10](https://ns-3-dce.readthedocs.io/en/dce-1.10/getting-started.html)
- [ns-3.28](https://www.nsnam.org/doxygen/index.html)
- [mmWave](https://github.com/nyuwireless-unipd/ns3-mmwave)
- [MPTCP](https://www.multipath-tcp.org)

### Requirements
> pip 안깔려 있으면 설치 `sudo apt-get install python-pip`  
> python setup tools 업그레이드 `pip install --upgrade setuptools`  
> GCC-5, G++-5 버전 설치
```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install gcc-5 g++-5

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave /usr/bin/g++ g++ /usr/bin/g++-5
```

### Environment
> Ubuntu 14.04.5  
> GCC-5, G++-5  
> DCE-1.10  

### Sequence
1. Install bake program  
```
cd $HOME
hg clone http://code.nsnam.org/bake bake
export BAKE_HOME=`pwd`/bake
export PATH=$PATH:$BAKE_HOME
export PYTHONPATH=$PYTHONPATH:$BAKE_HOME
```
2. Create DCE folder
```
mkdir dce
cd dce
```

3. Configure version of DCE and download DCE
```
bake.py configure -e dce-linux-1.10
bake.py download
```

4. Replace ns-3.28 folder to mmwave module
```
cd $HOME/dce/source
sudo rm -r ns-3.28
git clone https://github.com/parksjin01/temp_ns3-mmwave.git
mv temp_ns3-mmwave ns-3.28
```

5. Apply patch files
```
cd $HOME/dce/source/ns-3-dce/model
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/patch.diff
patch < patch.diff
```

6. Modify some files and build with bake
```
cd $HOME/dce/source/ns-3-dce
rm wscript
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/wscript

cd model
rm unix-datagram-socket-fd.cc
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/unix-datagram-socket-fd.cc

cd ../test/addons
rm dce-linux-ip6-test.cc
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/dce-linux-ip6-test.cc

cd $HOME/dce/source/ns-3.28/src/mmwave/model
rm mmwave-beamforming.cc
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/mmwave-beamforming.cc

cd $HOME/dce
bake.py build
```

7. Replace net-next-nuse-4.4.0 folder
```
cd $HOME/dce/source
sudo rm -r net-next-nuse-4.4.0
git clone -b mptcp_trunk_libos https://github.com/libos-nuse/net-next-nuse.git
mv net-next-nuse net-next-nuse-4.4.0
```

8. Configure new net-next-nuse-4.4.0 folder and compile
```
cd $HOME/dce/source/net-next-nuse-4.4.0
cat >> arch/lib/defconfig <<END
CONFIG_MPTCP=y
CONFIG_MPTCP_PM_ADVANCED=y
CONFIG_MPTCP_FULLMESH=y
CONFIG_MPTCP_NDIFFPORTS=y
CONFIG_DEFAULT_FULLMESH=y
CONFIG_DEFAULT_MPTCP_PM="fullmesh"
CONFIG_MPTCP_SCHED_ADVANCED=y
CONFIG_MPTCP_ROUNDROBIN=y
CONFIG_DEFAULT_MPTCP_SCHED="default"
END

make defconfig ARCH=lib
make library ARCH=lib
mv liblinux.so liblinux0.so
ln -s $HOME/dce/source/net-next-nuse-4.4.0/arch/lib/tools/libsim-linux.so $HOME/dce/source/net-next-nuse-4.4.0/liblinux.so
```

9. Install and patch new iproute2 program
```
wget http://ftp.osuosl.org/pub/clfs/conglomeration/iproute2/iproute2-2.6.38.tar.bz2
tar jxf iproute2-2.6.38.tar.bz2
cd iproute2-2.6.38
cp $HOME/dce/source/ns-3-dce/utils/iproute-2.6.38-fix-01.patch ./
patch -p1 -i iproute-2.6.38-fix-01.patch
rm Makefile
wget https://raw.githubusercontent.com/parksjin01/2018_USA/master/Modification/Makefile
make clean
LDFLAGS=-pie make CCOPTS='-fpic -D_GNU_SOURCE -O0 -U_FORTIFY_SOURCE'
```

10. Reconfigure DCE
```
export DCE_PATH=$HOME/dce/source/net-next-nuse-4.4.0:$HOME/dce/source/iproute2-2.6.38/ip
cd $HOME/dce/source/ns-3-dce
./waf configure --with-ns3=$HOME/dce/build --enable-kernel-stack=$HOME/dce/source/net-next-nuse-4.4.0/arch --prefix=$HOME/dce/build
./waf build
```
