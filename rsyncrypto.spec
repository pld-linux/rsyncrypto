#
# TODO:
# - fix descriptions and summaries to reflect that it isn't rsync but rsyncrypto
#
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	Ёвф╝©Же╘╦╕ еКгя фдюо╣©╠Бх╜╦╕ ю╖гя га╥н╠в╥╔
Summary(pl):	Program do wydajnego zdalnego uaktualniania plikСw
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	Программа для эффективного удаленного обновления файлов
Summary(uk):	Програма для ефективного в╕ддаленого оновлення файл╕в
Summary(zh_CN):	[м╗я╤]╢╚йД╧╓╬ъ
Summary(zh_TW):	[ЁЯ╟т]$(B6G?i╓У(c(B
Name:		rsyncrypto
Version:	0.17
Release:	0.5
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/rsyncrypto/%{name}-%{version}.tar.gz
# Source0-md5:	b04df4561d5f9847b647f9c60912d2af
URL:		http://rsync.samba.org/
BuildRequires:	argtable2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -l es
rsync es un substituto mАs rАpido y flexible para rcp que permite la
sincronizaciСn de archivos o directorios, vМa red, de forma rАpida y
eficiente, entre diferentes mАquinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las mАquinas tengan una copia de lo que estА en la
otra. EstА disponible en este paquete, una relaciСn tИcnica
describiendo el algoritmo usado por el rsync.

%description -l ko
Rsync╢б ©Ь╟щ хё╫╨ф╝ фдюою╩ ╦е©Л ╩║╦╝ ╣©╠Бх╜го╢б╣╔ ╫е╥згр╦╦гя
╬к╟М╦╝аРю╩ ╩Г©Кгя╢ы. Rsync╢б фдюоюг юЭц╪╦╕ ╨╦Ё╩╢б ╟м ╢К╫е©║ Ёвф╝©Вю╩
еКгь фдюоюг ╢ы╦╔ ╨н╨п╦╦ю╩ юЭ╪шго╠Б ╤╖╧╝©║ ╨Э╦ё╢ы. Rsync╢б ╟╜╥бгя ╧л╥╞
га╥н╪╪╫╨ х╓ю╨ rcp д©╦Ю╣Е╦╕ еКгя ╢У ©Л╪Жгя ╢Кц╪©Кю╦╥н╫А ╩Г©К╣х╢ы. rsync
╬к╟М╦╝аРю╩ ╧╕╩Гго╢б ╠Б╪ЗюШюн Ё╩©Кю╨ юл ╡ы╥╞╧л©║ фВгт╣г╬Н юж╢ы.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan╠ skЁadni╠
poleceЯ. Program ten u©ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plikСw do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zostaЁa rСwnie© doЁ╠czona do pakietu.

%description -l pt_BR
O rsync И um substituto mais rАpido e flexМvel para o rcp permitindo
sincronizaГЦo de arquivos ou diretСrios via rede de forma rАpida e
eficiente entre diferentes mАquinas transferindo somente as diferenГas
entre estes diretСrios de forma compactada. Ele nЦo precisa que
nenhuma das mАquinas tenha uma cСpia do que estА na outra.

Um relatСrio tИcnico descrevendo o algoritmo usado pelo rsync estА
disponМvel neste pacote.

%description -l ru
rsync - это более быстрая и гибкая альтернатива rcp, позволяющая
быструю и эффективную по отношению к ресурсам сети синхронизацию
файлов или каталогов на различных машинах путем передачи только
различий между ними в компрессированном виде. При этом совершенно не
обязательно, чтобы одна машина имела у себя копию того, что есть на
другой машине.

%description -l uk
rsync - це швидша та гнучк╕ша альтернатива rcp, яка забезпечу╓ швидку
та ефективну по в╕дношенню до ресурс╕в мереж╕ синхрон╕зац╕ю файл╕в чи
каталог╕в на р╕зних машинах шляхом передач╕ лише в╕дм╕нностей м╕ж ними
в компресованому вид╕. При цьому зовс╕м не обов'язково, щоб одна
машина мала в себе коп╕ю того, що ╓ на ╕нш╕й машин╕.

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
