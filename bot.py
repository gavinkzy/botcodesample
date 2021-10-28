@bot.command(brief='Gets champ info.')
async def aram(ctx, champ=None):
    champ = findChampName(champ)
    embedVar = discord.Embed(description="Recommended Aram Builds For " +str(champ), color= 0xf2f2f2)
    embedVar.set_author(name="u.gg", icon_url="https://cdn.discordapp.com/attachments/856429036078628864/901168169929023548/X1Daf_aS.png")
    if champ != None:
        try:
            champ_url = "https://static.u.gg/assets/lol/riot_static/11.21.1/data/en_US/champion/{champ}.json".format(champ=champ)
            r = requests.get(url=champ_url, headers=headers,  auth=HTTPBasicAuth('username', 'password'))
            champ_id = r.json()['data'][champ]['key']

            data_get_url = "https://stats2.u.gg/lol/1.1/overview/11_21/normal_aram/{champ_id}/1.5.0.json".format(champ_id=champ_id)
            r_data = requests.get(url=data_get_url, headers=headers, auth=HTTPBasicAuth('username', 'password'))
            data_json = r_data.json()
            rec_spell_order_list = data_json['1']['8']['6'][0][4][2]
            rec_spell_order_str = ""
            count = 1
            for each in rec_spell_order_list:
                if rec_spell_order_str == "":
                    rec_spell_order_str += each
                    count += 1
                else:
                    if each == "R":
                        rec_spell_order_str = rec_spell_order_str + " → " + each + "[{num}]".format(num=str(count))
                    else:
                        rec_spell_order_str = rec_spell_order_str + " → " + each
                    count += 1

            rec_runes = data_json['1']['8']['6'][0][0][4]
            rec_runes_str = ""
            for each in rec_runes:
                rune_name = runes_dict[each]
                if rec_runes_str == "":
                    rec_runes_str = rune_name
                else:
                    rec_runes_str = rec_runes_str + " | " +str(rune_name)

            starting_items_list = data_json['1']['8']['6'][0][2][2]
            core_items_list = data_json['1']['8']['6'][0][3][2]
            fourth_items_list = data_json['1']['8']['6'][0][5][0]
            fifth_items_list = data_json['1']['8']['6'][0][5][1]
            sixth_items_list = data_json['1']['8']['6'][0][5][2]
            #Get Starting Items
            starting_items_str = ""
            for each in starting_items_list:
                starting_items_str = starting_items_str + "\n" + items_dict[str(each)]

            #Get Core Items
            core_items_str = ""
            for each in core_items_list:
                core_items_str = core_items_str + "\n" + items_dict[str(each)]

            #Get Fourth Items
            fourth_items_str = ""
            for each in fourth_items_list:
                fourth_items_str = fourth_items_str + "\n" +items_dict[str(each[0])]

            #Get Fifth Items
            fifth_items_str = ""
            for each in fifth_items_list:
                fifth_items_str = fifth_items_str + "\n" +items_dict[str(each[0])]

            #Get Sixth Items
            sixth_items_str = ""
            for each in sixth_items_list:
                sixth_items_str = sixth_items_str + "\n" +items_dict[str(each[0])]

            direct_link = "https://u.gg/lol/champions/aram/" + str(champ).lower() + "-aram"

            embedVar.add_field(name=":magic_wand: Spell Order", value=rec_spell_order_str, inline=False)
            embedVar.add_field(name=":boxing_glove: Runes", value=rec_runes_str, inline=False)
            embedVar.add_field(name=":arrow_right: Starting Items", value=starting_items_str, inline=True)
            embedVar.add_field(name=":twisted_rightwards_arrows: Core Items", value=core_items_str, inline=True)
            embedVar.add_field(name=":four: Fourth Buy", value=fourth_items_str, inline=True)
            embedVar.add_field(name=":five: Fifth Buy", value=fifth_items_str, inline=True)
            embedVar.add_field(name=":six: Sixth Buy", value=sixth_items_str, inline=True)
            embedVar.add_field(name=":paperclips: ", value=direct_link, inline=False)
            embedVar.set_image(url="https://static.u.gg/assets/lol/riot_static/11.21.1/img/champion/{champ}.png".format(champ=champ))
            #embedVar.set_footer(text=direct_link)
            print("Fetched from u.gg.")
            await ctx.send(embed=embedVar)
        except:
            await ctx.send("An error has occurred.")
    else:
        await ctx.send("Please input a champion name.")