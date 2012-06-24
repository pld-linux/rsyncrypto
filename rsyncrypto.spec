#
# TODO:
# - fix descriptions and summaries to reflect that it isn't rsync but rsyncrypto
#
Summary:	Program for efficient remote updates of files
Summary(es.UTF-8):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko.UTF-8):	네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl.UTF-8):	Program do wydajnego zdalnego uaktualniania plików
Summary(pt_BR.UTF-8):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru.UTF-8):	Программа для эффективного удаленного обновления файлов
Summary(uk.UTF-8):	Програма для ефективного віддаленого оновлення файлів
Summary(zh_CN.UTF-8):	[通讯]传输工具
Summary(zh_TW.UTF-8):	[喙啪]$(B6G?i火(c(B
Name:		rsyncrypto
Version:	0.17
Release:	0.6
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/rsyncrypto/%{name}-%{version}.tar.gz
# Source0-md5:	b04df4561d5f9847b647f9c60912d2af
URL:		http://rsync.samba.org/
BuildRequires:	argtable2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	gzip(rsyncable)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -l es.UTF-8
rsync es un substituto más rápido y flexible para rcp que permite la
sincronización de archivos o directorios, vía red, de forma rápida y
eficiente, entre diferentes máquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las máquinas tengan una copia de lo que está en la
otra. Está disponible en este paquete, una relación técnica
describiendo el algoritmo usado por el rsync.

%description -l ko.UTF-8
Rsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Rsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Rsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. rsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl.UTF-8
Rsync jest zamiennikiem programu rcp z bardziej rozbudowaną składnią
poleceń. Program ten używa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plików do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu została również dołączona do pakietu.

%description -l pt_BR.UTF-8
O rsync é um substituto mais rápido e flexível para o rcp permitindo
sincronização de arquivos ou diretórios via rede de forma rápida e
eficiente entre diferentes máquinas transferindo somente as diferenças
entre estes diretórios de forma compactada. Ele não precisa que
nenhuma das máquinas tenha uma cópia do que está na outra.

Um relatório técnico descrevendo o algoritmo usado pelo rsync está
disponível neste pacote.

%description -l ru.UTF-8
rsync - это более быстрая и гибкая альтернатива rcp, позволяющая
быструю и эффективную по отношению к ресурсам сети синхронизацию
файлов или каталогов на различных машинах путем передачи только
различий между ними в компрессированном виде. При этом совершенно не
обязательно, чтобы одна машина имела у себя копию того, что есть на
другой машине.

%description -l uk.UTF-8
rsync - це швидша та гнучкіша альтернатива rcp, яка забезпечує швидку
та ефективну по відношенню до ресурсів мережі синхронізацію файлів чи
каталогів на різних машинах шляхом передачі лише відмінностей між ними
в компресованому виді. При цьому зовсім не обов'язково, щоб одна
машина мала в себе копію того, що є на іншій машині.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
