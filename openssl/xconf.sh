case "$TARGET" in
    "")
        echo "TARGET is not set" >&2
        exit 5
        ;;
    i686-*)
        OS="linux-generic32";;
    arm-*)
        OS="linux-armv4";;
    *)
        echo "Unknown target: '$TARGET'" >&2
        exit 5
        ;;
esac

./Configure no-dso no-krb5 $OS --prefix=../thirdparty --openssldir=../openssl
